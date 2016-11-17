#!/usr/bin/env python

import cv2
import os
import numpy as np
import argparse
import plantcv as pcv
from plantcv.dev.color_palette import color_palette


def options():
    parser = argparse.ArgumentParser(description="Imaging processing with opencv")
    parser.add_argument("-i", "--image", help="Input image file.", required=True)
    parser.add_argument("-o", "--outdir", help="Output directory for image files.", default=".")
    parser.add_argument("-m", "--mask", help="mask for image", default="./sample-data/seed-mask.jpg")
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

    device, img1 = pcv.white_balance(device, img, debug, (100, 100, 1000, 1000))
    img = img1

    seedmask, path1, filename1 = pcv.readimage(args.mask)
    device, seedmask = pcv.rgb2gray(seedmask, device, debug)
    device, inverted = pcv.invert(seedmask, device, debug)
    device, masked_img = pcv.apply_mask(img, inverted, 'white', device, debug)

    device, img_gray_sat = pcv.rgb2gray_hsv(masked_img, 's', device, debug)

    device, img_binary = pcv.binary_threshold(img_gray_sat, 50, 255, 'light', device, debug)

    img_binary1 = np.copy(img_binary)
    device, fill_image = pcv.fill(img_binary1, img_binary, 300, device, debug)

    device, seed_objects, seed_hierarchy = pcv.find_objects(img, fill_image, device, debug)

    device, roi1, roi_hierarchy1 = pcv.define_roi(img, 'rectangle', device, None, 'default', debug, True,
                                                  1800, 1600, -1500, -500)

    device, roi_objects, roi_obj_hierarchy, kept_mask, obj_area = pcv.roi_objects(img, 'partial', roi1, roi_hierarchy1,
                                                                                  seed_objects, seed_hierarchy, device,
                                                                                  debug)

    img_copy = np.copy(img)
    for i in range(0, len(roi_objects)):
        rand_color = color_palette(1)
        cv2.drawContours(img_copy, roi_objects, i, rand_color[0], -1, lineType=8, hierarchy=roi_obj_hierarchy)

    pcv.print_image(img_copy, os.path.join(args.outdir, filename[:-4]) + "-seed-confetti.jpg")

    shape_header = []  # Store the table header
    table = []  # Store the PlantCV measurements for each seed in a table
    for i in range(0, len(roi_objects)):
        if roi_obj_hierarchy[0][i][3] == -1:  # Only continue if the object is an outermost contour

            # Object combine kept objects
            # Inputs:
            #    contours = object list
            #    device   = device number. Used to count steps in the pipeline
            #    debug    = None, print, or plot. Print = save to file, Plot = print to screen.
            device, obj, mask = pcv.object_composition(img, [roi_objects[i]], np.array([[roi_obj_hierarchy[0][i]]]),
                                                       device, None)
            if obj is not None:
                # Measure the area and other shape properties of each seed
                # Inputs:
                #    img             = image object (most likely the original), color(RGB)
                #    imgname         = name of image
                #    obj             = single or grouped contour object
                #    device          = device number. Used to count steps in the pipeline
                #    debug           = None, print, or plot. Print = save to file, Plot = print to screen.
                #    filename        = False or image name. If defined print image
                device, shape_header, shape_data, shape_img = pcv.analyze_object(img, "img", obj, mask, device, None)

                if shape_data is not None:
                    table.append(shape_data[1])

    data_array = np.array(table)
    maxval = np.argmax(data_array)
    maxseed = np.copy(img)
    cv2.drawContours(maxseed, roi_objects, maxval, (0, 255, 0), 50)

    imgtext = "This image has " + str(len(data_array)) + " seeds"
    sizeseed = "The largest seed is in green and is " + str(data_array[maxval]) + " pixels"
    cv2.putText(maxseed, imgtext, (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 10)
    cv2.putText(maxseed, sizeseed, (500, 1000), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 255), 10)
    pcv.print_image(maxseed, os.path.join(args.outdir, filename[:-4]) + "-maxseed.jpg")


if __name__ == '__main__':
    main()
