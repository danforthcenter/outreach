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
    parser.add_argument("-D", "--debug", help="Turn on debug, prints intermediate images.",default=None)
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

    device, corrected_img = pcv.white_balance(device, img, debug, (500, 1000, 500, 500))
    img = corrected_img

    device, img_gray_sat = pcv.rgb2gray_lab(img, 'a', device, debug)

    device, img_binary = pcv.binary_threshold(img_gray_sat, 120, 255, 'dark', device, debug)

    mask = np.copy(img_binary)
    device, fill_image = pcv.fill(img_binary, mask, 300, device, debug)

    device, id_objects, obj_hierarchy = pcv.find_objects(img, fill_image, device, debug)

    device, roi, roi_hierarchy = pcv.define_roi(img, 'rectangle', device, None, 'default', debug, True,
                                                1800, 2000, -1500, -500)

    device, roi_objects, roi_obj_hierarchy, kept_mask, obj_area = pcv.roi_objects(img, 'partial', roi, roi_hierarchy,
                                                                                  id_objects, obj_hierarchy, device,
                                                                                  debug)

    device, obj, mask = pcv.object_composition(img, roi_objects, roi_obj_hierarchy, device, debug)

    outfile = os.path.join(args.outdir, filename)

    device, color_header, color_data, color_img = pcv.analyze_color(img, img, mask, 256, device, debug, None, 'v',
                                                                    'img', 300, outfile)

    device, shape_header, shape_data, shape_img = pcv.analyze_object(img, "img", obj, mask, device, debug, outfile)

    shapepath = outfile[:-4] + '_shapes.jpg'
    shapepic = cv2.imread(shapepath)
    plantsize = "The plant is " + str(np.sum(mask)) + " pixels large"
    cv2.putText(shapepic, plantsize, (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 10)
    pcv.print_image(shapepic, outfile[:-4] + '-out_shapes.jpg')


if __name__ == '__main__':
    main()

