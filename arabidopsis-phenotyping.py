#!/usr/bin/env python

import cv2
import os
import numpy as np
import argparse
import plantcv as pcv


def options():
    parser = argparse.ArgumentParser(description="Imaging processing with opencv")
    parser.add_argument("-i", "--image", help="Input image file.", required=True)
    parser.add_argument("-o", "--outdir", help="Output directory for image files.", default=".")
    parser.add_argument("-w", "--writeimg", help="write out images.", default=False, action="store_true")
    parser.add_argument("-D", "--debug", help="Turn on debug, prints intermediate images.", default=None)
    args = parser.parse_args()
    return args


# Main pipeline
def main():
    # Get options
    args = options()

    debug = args.debug

    # Read image
    img, path, filename = pcv.readimage(args.image)

    # Pipeline step
    device = 0

    device, img1 = pcv.white_balance(device, img, debug, roi=(1000, 1000, 500, 500))

    device, a = pcv.rgb2gray_lab(img1, 'a', device, debug)

    device, img_binary = pcv.binary_threshold(a, 116, 255, 'dark', device, debug)

    mask = np.copy(img_binary)
    device, fill_image = pcv.fill(img_binary, mask, 300, device, debug)

    device, id_objects, obj_hierarchy = pcv.find_objects(img1, fill_image, device, debug)

    device, roi, roi_hierarchy = pcv.define_roi(img1, 'rectangle', device, None, 'default', debug, True,
                                                1800, 1600, -1500, -500)

    device, roi_objects, roi_obj_hierarchy, kept_mask, obj_area = pcv.roi_objects(img1, 'partial', roi, roi_hierarchy,
                                                                                  id_objects, obj_hierarchy, device,
                                                                                  debug)

    outfile = os.path.join(args.outdir, filename)

    device, color_header, color_data, color_img = pcv.analyze_color(img1, img1, kept_mask, 256, device, debug, None,
                                                                    'v', 'img', 300, outfile)

    device, masked = pcv.apply_mask(img1, kept_mask, 'white', device, debug)
    device, dilated = pcv.dilate(kept_mask, 10, 2, device, debug)
    device, plant_objects, plant_hierarchy = pcv.find_objects(img1, dilated, device, debug)

    img_copy = np.copy(img1)

    color = [(255, 0, 255), (0, 255, 0), (66, 134, 244), (255, 255, 0)]

    for i in range(0, len(plant_objects)):
        if len(plant_objects[i]) < 100:
            pass
        else:
            background = np.zeros((np.shape(img1)), np.uint8)
            cv2.drawContours(background, plant_objects, i, (255, 255, 255), -1, lineType=8, hierarchy=plant_hierarchy)
            device, grayimg = pcv.rgb2gray(background, device, debug)
            device, masked1 = pcv.apply_mask(masked, grayimg, 'white', device, debug)
            device, a1 = pcv.rgb2gray_lab(masked1, 'a', device, debug)
            device, img_binary1 = pcv.binary_threshold(a1, 116, 255, 'dark', device, debug)
            device, single_object, single_hierarchy = pcv.find_objects(masked1, img_binary1, device, debug)
            device, obj, mask = pcv.object_composition(img1, single_object, single_hierarchy, device, debug)
            device, shape_header, shape_data, shape_img = pcv.analyze_object(img, "img", obj, mask, device, debug)
            cv2.drawContours(img_copy, plant_objects, i, color[i], -1, lineType=8, hierarchy=plant_hierarchy)
            plantsize = "Plant matching this color is " + str(shape_data[1]) + " pixels large"
            cv2.putText(img_copy, plantsize, (500, (i + 1) * 300), cv2.FONT_HERSHEY_SIMPLEX, 5, color[i], 10)

    pcv.print_image(img_copy, os.path.join(args.outdir, "arabidopsis-out_shapes.jpg"))

if __name__ == '__main__':
    main()

