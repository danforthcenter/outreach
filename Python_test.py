#!/usr/bin/env python

print "hello world"

x="My name is "
y="Malia"
print x+y

### This script reads in two plant images and finds the absolute difference between them.
import plantcv as pcv
import numpy as np
import cv2

img1=cv2.imread("/home/pi/csiw_2015/outreach/sample_images/brachypodium/img1.png")
img2=cv2.imread("/home/pi/csiw_2015/outreach/sample_images/brachypodium/img2.png")
img3=cv2.absdiff(img1,img2)
pcv.print_image(img3,"/home/pi/plant1.jpg")
img4=cv2.bitwise_not(img3)
pcv.print_image(img4,"/home/pi/plant2.jpg")

### This script reads in two cat images and finds the absolute difference between them.
import plantcv as pcv
import numpy as np
import cv2

img1=cv2.imread("/home/pi/csiw_2015/outreach/sample_images/meowming/IMG_1490.JPG")
img2=cv2.imread("/home/pi/csiw_2015/outreach/sample_images/meowming/IMG_1491.JPG")

img3=cv2.absdiff(img2,img1)
pcv.print_image(img3,"/home/pi/meow1.jpg")
img4=cv2.bitwise_not(img3)
pcv.print_image(img4,"/home/pi/meow2.jpg")


###This is a sample of passing a user argument
#import argparse
#
#def options():
#  parser = argparse.ArgumentParser(description="Using Argparse")
#  parser.add_argument("-u", "--user", help="username.", required=True)
#  args = parser.parse_args()
#  return args
#
#def main():
#  # Get options
#  args = options()
#  
#  x="Hello, "+str(args.user)
#  print x
#  
#if __name__ == '__main__':
#  main()#!/usr/bin/env python
  
#This is a sample of passing a user argument
import argparse
import cv2
import plantcv as pcv
import numpy as np

def options():
  parser = argparse.ArgumentParser(description="Using Argparse")
  parser.add_argument("-i1", "--image1", help="path to image1.", required=True)
  parser.add_argument("-i2", "--image2", help="path image2.", required=True)
  parser.add_argument("-o", "--outdir", help="where to save the images.", required=True)
  args = parser.parse_args()
  return args

def main():
  # Get options
  args = options()
  
  img1=cv2.imread(args.image1)
  img2=cv2.imread(args.image2)

  img3=cv2.absdiff(img2,img1)
  
  path1=str(args.outdir)+"meow3.jpg"
  path2=str(args.outdir)+"meow4.jpg"
  pcv.print_image(img3,path1)
  img4=cv2.bitwise_not(img3)
  pcv.print_image(img4,path2)
  
if __name__ == '__main__':
  main()#!/usr/bin/env python


