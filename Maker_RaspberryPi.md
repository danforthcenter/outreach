# Maker Session: Working with Raspberry Pi

In this session we will learn to work with Raspberry Pi computers and the Raspberry Pi camera module. Raspberry Pi computers are small, single-board computers that cost between $20-35. The Raspberry Pi computers you will work with today are Pi 2 Model B ($35, 4-core ARM CPU, 1GB RAM) [Link](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/). Our Raspberry Pis are running a Linux operating system "Raspbian" which is a fork of Debian 7 "Wheezy." 

# Outline
1. Basic Linux operations
2. Using the Raspberry Pi camera

# Basic Linux operations

In addition to the command-line interface, Raspberry Pi computers can run a desktop environment. To start it type:

```
startx
```

From the desktop you can run a terminal program to continue to use the command-line interface.

## Basic Linux shell commands

**pwd** - print the current working directory path

**ls** - list the files and directories in the current working directory

**cd** - change directories directly to *home*

**cd** ***dir*** - change directories from the current working directory to *dir*

**touch** ***file*** - create the empty file *file*

**rm** ***file*** - remove the file *file*

**mkdir** ***dir*** - make the directory *dir*

**rmdir** ***dir*** - remove the directory *dir* (has to be empty)

**cp** ***file1*** ***file2*** - create a copy of *file1* called *file2*

**cp -r** ***dir1*** ***dir2*** - create a copy of *dir1* and its contents called *dir2*

**mv** ***file1*** ***file2*** - move/rename *file1* to *file2*

**head** ***file*** - print the first 10 lines of *file* to *stdout*

**tail** ***file*** - print the last 10 lines of *file* to *stdout*

**less** ***file*** - opens *file* using a paging viewer

**htop** - display the current running processes (task manager/activity monitor). It is a modern version of **top** which should be available if **htop** is not.

**df -h** - display disk usage with human-readable units

**gzip** ***file*** - compress *file*

**gunzip** ***file.gz*** - decompress *file.gz*

**tar zcf** ***archive.tar.gz*** ***dir*** - create a compressed archive of *dir* (or a set of files)

**tar zxf** ***archive.tar.gz*** - decompress and extract the contents of *archive.tar.gz*

**Ctrl+C** - stop the current command

**exit** - log out of the current session

## Log in to a remote Linux server

The most common method to log into a remote Linux computer (through the command line) is to use Secure Shell (ssh). For example:

```
ssh username@host.domain.com
```

# Using the Raspberry Pi camera

The Raspberry Pi camera module is a 5 megapixel, fixed-focus camera add-on for the Raspberry Pi. Each of your Raspberry Pi computers has a camera module installed. Your camera module is the Pi NoIR model (the infrared filter has been removed).

## Take a picture

To take a picture, see it, and save it with the name *image.jpg* use the following command:

```
raspistill –o image.jpg
```

## Save images to a directory

The image *image.jpg* is saved to your current working directory. Instead you might want to save images to a directory.

```
mkdir images
raspistill –o /home/pi/images/image.jpg
```

## Save images with unique names and some metadata

To take a picture, see it, and save it with the time stamp in front of the name image.jpg in the directory images in your home folder use the following command: 

```
raspistill -o /home/pi/images/$(date +"\%Y-\%m-\%d_\%H:\%M:\%S")_images.jpg
```

## Use cron to take images on a schedule (time-lapse)

Crontab is an easy way to schedule repeating tasks, like time-lapse imaging.

```
crontab -e
```

Crontab file format:

```
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * command to be executed
```

If you add the following line to crontab, what would it do?

```
0 * * * * /usr/bin/raspistill -o /home/pi/images/$(date +"%Y-%m-%d_%H:%M:%S")_timelapse.jpg
```

Can I test my commands before putting them into crontab?
- Yes! Just run them on the command line first in the terminal!!!!
- Why use crontab?
  - It will automatically run task as scheduled, even after reboot!
  - Time is set after booting and internet access, but if no internet, it will set time to last available time, which can cause problems. Hope you have wifi!!!!
  - Alt: can hardwire a clock with battery.


