# Using the Raspberry Pi camera

The Raspberry Pi camera module is a 5 megapixel (8 megapixel are now available), fixed-focus camera add-on for the Raspberry Pi. Each of your Raspberry Pi computers has a camera module installed. Your camera module is the Pi NoIR model (the infrared filter has been removed).

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
raspistill -o /home/pi/images/$(date +"%Y-%m-%d_%H:%M:%S")_images.jpg
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
0 * * * * /usr/bin/raspistill -o /home/pi/images/$(date +"\%Y-\%m-\%d_\%H:\%M:\%S")_timelapse.jpg
```

Can I test my commands before putting them into crontab?
- Yes! Just run them on the command line first in the terminal!!!!
- Why use crontab?
  - It will automatically run task as scheduled, even after reboot!
  - Time is set after booting and internet access, but if no internet, it will set time to last available time, which can cause problems. Hope you have wifi!!!!
  - Alt: can hardwire a clock with battery.