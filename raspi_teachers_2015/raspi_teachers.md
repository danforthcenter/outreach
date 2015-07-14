# DDPSC Raspberry Pi Teacher's Workshop: Working with Raspberry Pi

##Introduction to Raspberry Pi

*  See slide decks [here](https://github.com/danforthcenter/outreach/tree/master/raspi_teachers_2015/Presentations)
*  See these websites for more information on how to use Raspberry Pis:
    *  [https://www.raspberrypi.org/](https://www.raspberrypi.org/)
    *  [http://sonic-pi.net/](http://sonic-pi.net/)
    *  [https://learn.adafruit.com/category/raspberry-pi](https://learn.adafruit.com/category/raspberry-pi)
    *  [http://www.raspberrypitutorials.yolasite.com/](http://www.raspberrypitutorials.yolasite.com/)

##Putting the Operating System (OS) on the Raspberry Pi
In this session we will learn to work with Raspberry Pi computers and later the Raspberry Pi camera module. Raspberry Pi computers are small, single-board computers that cost between $20-35.
The Raspberry Pi computers you will work with today are Pi 2 Model B ($35, 4-core ARM CPU, 1GB RAM) [Link](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/).
Our Raspberry Pis are running a Linux operating system "Raspbian" which is a fork of Debian 7 "Wheezy." The operating system is on the microSD card in your Pi. We've 'flashed' the cards for you
but if you want to do one yourself you can download the operating system from the [Raspberry Pi website](https://www.raspberrypi.org/downloads/). For Mac users we recommend using the free program
ApplePi-Baker that is available [here](http://www.tweaking4all.com/hardware/raspberry-pi/macosx-apple-pi-baker/) putting a disk image on a card, scroll down to download the **non-sudo version**.
For Windows users, options for flashing cards can be found [here](http://www.tweaking4all.com/hardware/raspberry-pi/install-img-to-sd-card/#windows).  

##Next we will set up the Raspberry Pi configurations

For more information see the [Raspberry Pi Github Page](/github.com/raspberrypi/documentation/blob/master/configuration/README.md). There will be more on using GitHub later.


In addition to the command-line interface, Raspberry Pi computers can run a desktop environment. To start it type after logging in:

```
startx
```

##Basic Linux operations  

What is Linux?: Linux is an operating system, which is software that supports basic computer functions.
Other examples of operating systems are Unix, Mac OS, Windows XP or Windows 7. You can do things like,
make files, move files, copy files, make directories (folders) etc. etc. but instead of seeing icons like a Windows or Mac interface you would use text (the command line).


From the desktop you can run a terminal program to continue to use the command-line interface (called LXTerminal).

##Basic Linux shell commands  

If you need help on how/why to use a command the best thing to do is to google it.  

**pwd** - print the current working directory path. The "working directory" means the folder you are currently in.  

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


##Introduction to Github and other websites of interest.

*  [Github](https://github.com/): Github is a way to code collaboratively, or to find code to jumpstart your project. Github + Jekyll + Markdown is also an easy way to set up a website for your projects. 


To clone a repository in LXterminal type:

```

git clone https://github.com/danforthcenter/outreach.git

```

We won't be doing this today, but you can also add data to a repository if you've made changes.

Four steps add data to a repository (that you have permissions to you can also do a 'pull' request that is asking for permission to push):

1)  To add data to a repository: (make sure you are in right folder)

```
# the . means to add all
# instead of adding all you can add specific files
git add .

```

2)  To commit data to a repository:

```
# commit the additions to the repository
# minimally needs a metadata message
git commit -m "adding new data to this repository"

```

3)  Pull the repository to merge your committed changes with the newest version of the repository.

```
# make sure your version of the files are up to date before you try to add new things to the repository
git pull

```

4)  Push your data to the repository.

```
# push your new data to the repository
git push

```

Other important websites:
*  Thingiverse has lots of patterns to 3D print [here](https://www.thingiverse.com/)
*  Raspberry Pis are computers but Arduino microcontrollers are also very useful for projects [here](https://www.arduino.cc/)
*  OpenScad is a free program to design 3D objects [here](http://www.openscad.org/)
*  More info on Github pages [here](https://pages.github.com/)
*  Jekyll is a tool to help develop your website with Github [here](https://help.github.com/articles/using-jekyll-with-pages/)

##Pi passwords and backing up files

The OS Raspbian comes with a single preconfigured user account (username: pi, password: raspberry). The pi user account is a privileged user, meaning that it has the capability of installing software, modifying the computer settings, etc. This can be a great way to learn how to administer Linux systems but for a classroom setting it could potentially lead to accidental changes that could ruin a project. There are two complementary ways to address this problem.

###Secure the pi user account and create a student user account
1) Anyone on the internet can find the default username/password, so change the pi user password to something more secure.

```
passwd

# Follow the instructions to set a new password
```

2) Create a new student account. By default new users are not privileged users. As the pi user you have access to administrator (root) capabilities using the "sudo" command.

```
sudo useradd -b /home -m -g users student

# sudo lets the pi user execute the useradd command as the administrator
# -b sets the base location of the student user home directory
# -m tells useradd to create the home directory
# -g users sets the student account group to users
```

3) Set the password for the student account

```
sudo passwd student

# Follow the instructions to set a password for the student account.
# This is the same command you used to set the pi user password
# except that here you are using administrator privilege to set the
# password for another account.
```

###Create a backup of your Raspberry Pi SD card


##Introduction to Soldering

Soldering is basically like metal glue. We will be soldering a small IR light panel so that we can take images at night.

*  More on how to solder [here](https://learn.adafruit.com/adafruit-guide-excellent-soldering/tools)
*  And [here](https://github.com/danforthcenter/outreach/tree/master/raspi_teachers_2015/How%20to%20solder)


##Using the Raspberry Pi camera

The Raspberry Pi camera module is a 5 megapixel, fixed-focus camera add-on for the Raspberry Pi. Each of your Raspberry Pi computers has a camera module installed. Your camera module is the Pi NoIR model (the infrared filter has been removed).

## Take a picture

To take a picture, see it, and save it with the name *image.jpg* use the following command:

```python

# this command will take a picture but it will put it in whatever working directory (folder) you are in
# the -o tells the program what to name the image and also where to put it, if it is just the name it puts the image in whatever folder you are currently in.
raspistill -o image1.jpg

# To see where you've save the image (what folder you are currently in) type
pwd

# To see the names of the files in your current folder type
ls -l

```
**Pro-tip, if you want to rerun a command that you recently used, you can hit the uparrow to get to previous commands**

To actually view the image, you can go to the file folder icon on the desktop and open the file or on the command line...

```

display /home/pi/images/image1.jpg

```

##Flip a picture if it is upside down

Is your picture upsidedown when you look at it? If it is you will need to add the -vf (vertical flip) flag to your command.

```

raspistill -vf -o image1.jpg

```


## Save images to a directory

The image *image.jpg* is saved to your current working directory. Instead you might want to save images to a specific directory.

```
mkdir images

#now you've made a folder named images

raspistill -o /home/pi/images/image1.jpg

#The -o flag tells the raspistill program that you want to save the file to a specific place.
# remember if your camera is upsidedown to use the -vf flag.
```

## Save images with unique names and some metadata

To take a picture, see it, and save it with the time stamp in front of the name image.jpg in the directory images in your home folder use the following command: 

```

# if you add the timestamp to the name you can use the same command over and over again (gives the imaage a new name and doesn't overwrite)
# the name of the image below would include the current year, month, day, hour, min, and second
raspistill -o /home/pi/images/$(date +"%Y-%m-%d_%H:\%M:%S")_images.jpg

# now press the up arrow, the command you just ran should show up, take another picture.
```

## Take a time-lapse

After you take a few pictures and are satisfied with the setup you can take a time-lapse

```
# to take a timelapse you need to use the -tl option, which is the time between images, but the time is in milliseconds
# you also need the -t option, which tells the program how long to run timelapse
# the command below takes an image named using the timestamp every 3 seconds for 1 min
# We cannot use the timestamp to name the images because how the program is written, but we can use another way of naming the images
# by nameing the images image%05d.jpg we tell the program to give the image a 5 digit number at the end of the name
# So the first image would be named image00001.jpg

raspistill -t 60000 -tl 3000 -o /home/pi/images/image%05d.jpg 

```

## What happens if the computer shuts off during the time-lapse?  

In order to make sure that the computer will keep running the time-lapse if the computer shuts off you need to modify
crontab.

## Use cron to take images on a schedule (time-lapse)

Crontab is an easy way to schedule repeating tasks so it can be used as another way to do time-lapse imaging, like time-lapse imaging.

```
#First let's make another folder so that we don't confuse it with the first timelapse

mkdir /home/pi/timelapse2

#This opens up the crontab file in using the leafpad text editor program

sudo leafpad /etc/crontab
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

add the following line to the cron file (you should see a list of commands that also start with an astericks).

```
#this tells the command to run every 10 min of every hour every day of the month every day of the week.

*/10 * * * * pi /usr/bin/raspistill -o /home/pi/timelapse2/$(date +"\%Y-\%m-\%d_\%H:\%M:\%S")_timelapse.jpg

#save the file and close it

```

now we need to restart the cron to make sure the changes take effect. On the command line type

```

sudo service cron restart

```

Can I test my commands before putting them into crontab?
- Yes! Just run them on the command line first in the terminal!!!!
- Why use crontab?
  - It will automatically run task as scheduled, even after reboot!
  - Time is set after booting and internet access, but if no internet, it will set time to last available time, which can cause problems. Hope you have wifi!!!!
  - Alt: can hardwire a clock with battery.


## Assembling your time-lapse into a short movie

first we need to write all of image names into a text file, but we can do that using the command line  

```

# This takes all of jpg files in your current folder and writes their names to a file called stills.txt 

cd /home/pi/timelapse2/

ls *.jpg > stills.txt

#If you only wanted to use every other image (we won't be doing this)
awk 'NR%2==0' stills.txt > stills_even.txt

```  

now we can assemble the files into a time-lapse movie  


```
# -ocv tells the mencoder program what video format to use  
# -lavcopts tells the opctions you want for the video format (size etc.)
# -o tell the program what to name your file
# -mf tells the program what file format and the number of frames per second that you want, as well as the file with all the image names

mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o timelapse.avi -mf type=jpeg:fps=24 mf://@stills_even.txt

#if you need to flip your images
mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -flip -o timelapse.avi -mf type=jpeg:fps=24 mf://@stills_even.txt

```

To see your videos we will also add them to a playlist here

[playlist link](https://www.youtube.com/playlist?list=PLimbrUa_ArHwJ9n_HL_IQsU0pAGpnxtPD)

##Now let's move your movie to a folder with your name

```

#let's make a directory (folder) with your name (no spaces)

mkdir /home/pi/yourname

#for example: mkdir /home/pi/malia

# then let's list the files to see if your folder is there

ls -l /home/pi/

# you should see a folder with your name

#now let's move your timelapse.mp4 movie there, make sure you replace the "yourname" with your actual name

mv /home/pi/images/timelapse2/timelapse.mp4 /home/pi/yourname/timelapse.mp4

#check that the file is in there

ls -l /home/pi/yourname/

```

##Introduction to Raspberry Pi Sensors

There are numerous sensors that are available for Raspberry Pi computers and also for Arduino microcontrollers.

*  Adafruit has a nice selection of sensors and tutorials [here](http://www.adafruit.com/category/35)
*  The best way to find out how to use a sensor is to google it and find online tutorials.

We will be using four different 'sensor' modules today  
1)  Light panel: Bright Pi, more information [here](https://github.com/danforthcenter/outreach/tree/master/raspi_teachers_2015/Bright%20Pi%20assembly%20instructions)  
2)  Temperature sensor: More information [here](https://www.adafruit.com/product/1893)  
3)  Light sensor: More information [here](https://www.adafruit.com/products/439)

How to make your Raspberry pi more 'rugged'
*  Weather proofing in a coffee can by Jim at fotosyn [here](http://www.fotosyn.com/simple-timelapse-camera-using-raspberry-pi-and-a-coffee-tin/)
*  See post on 5 different cases [here](http://www.makeuseof.com/tag/5-ways-to-ruggedise-your-raspberry-pi/)
*  This Rustoleum coating might work [here](http://www.geek.com/chips/neverwet-makes-the-raspberry-pi-and-other-gadgets-waterproof-1564340/)

##Connecting a sensor to a Google doc

**More here from Noah**

##Opensource tools for image analysis

Collecting time lapse images are great for demonstrating concepts of plant growth, plant movement, and circadian rhythms.
But you might want to actually measure plant growth and plant movement. There are several opensource tools that make these measurements easier.

*  ImageJ is [here](http://fiji.sc/Fiji)
*  OpenCV (Open Computer Vision) is a library of image processing functions for a few languages (C/C++, Java, Python) that is widely used.  
There is documentation [here](http://opencv.org/). OpenCV is a very powerful library but it is not the most user friendly.
We built PlantCV (Plant Computer Vision) to process plant images specifically, building off of OpenCV and other available Python libraries.  
*  PlantCV documentation and information is located [here](http://plantcv.danforthcenter.org/)
*  R is a programming language that is used for statistical analysis, more information [here](http://www.r-project.org/)
*  R studio is a free graphical user interface (GUI) to make running R code easier. More info [here](https://www.rstudio.com/)

**Process images with PlantCV**

[PlantCV](http://plantcv.danforthcenter.org/) is software we wrote at the Danforth Center to extract biologically meaningful information from images of plants. Go to [here](http://plantcv.danforthcenter.org/pages/documentation/function_docs/vis_tutorial.html) for detailed instructions.

Pick an image and look at the name to determine which script to run most scripts are in dev (see example below) type:

```
path_to_script -i path_to_image -o destination_folder_for_output_images -D
```

For example:

```python

#The first part is the script that is being run.
#The -i is the path to the image you want analyzed
#The -o tells the program where to put the output images. A . means it will put the images in whatever directory you are currently in.
#The -D option at the end tells the program you are running it in debug mode, this means that every image at every step will get printed out (there are lots of steps, so lots of images)

/home/pi/plantcv/scripts/dev/vis_sv_z2500_L2_e82.py -i /home/pi/nsf_reu_workshop/sample_images/brachypodium/VIS_SV_0_z2500_h2_g0_e82_300296\ copy.png -o . -D

```

You just processed one image, you will see a bunch of information print out to the screen, and lots of new images appear in your working directory.
If you had many images to process you would then use the "parallelization" script, which runs the 'single image script' over a bunch of images and
then saves the data to a database. We won't be doing that today but the instructions are [here](http://plantcv.danforthcenter.org/pages/documentation/function_docs/vis_tutorial.html).
If you had run a full set of data (many plants growing over a period of time) you could then use R to analyze the data.

##Use R to analyze phenotyping data

R is a programming language that is used primarily for statistical analysis. To start R type:

```
R
```

You are now in an R console session. Import some R packages:

```r
library(ggplot2)
library(lubridate)
library(MASS)
```

Download a complete set of data for VIS images from the Danforth Center phenotyping system from Figshare. There were a total of 6,399 snapshots with VIS image data, but the download only includes the 6,207 snapshots that were successfully processed by PlantCV. Failed snapshots generally are those that lack a plant (empty pot controls, dead plants, etc.). The code below checks to see if the files exist and downloads them automatically if they do not.

```r
if (!file.exists('vis_snapshots_nocorrect.csv')) {
  download.file('http://files.figshare.com/2084100/vis_snapshots_nocorrect.csv',
                'vis_snapshots_nocorrect.csv')
}
```

Read the data from the CSV file. (This is saving the information into memory)

```r
vis.data = read.table(file="vis_snapshots_nocorrect.csv", sep=",", header=TRUE)
```

```r

#Now your data is saved to a variable named vis.data
#The function head, lets you view the first 10 lines of that table.

head(vis.data)

```

We need to format and label the data. The details in this section can be ignored for now.

```r
# Planting date
planting_date = as.POSIXct("2013-11-26")

# Add water treatment column coded in barcodes
vis.data$treatment <- NA
vis.data$treatment[grep("AA", vis.data$plant_id)] <- 100
vis.data$treatment[grep("AB", vis.data$plant_id)] <- 0
vis.data$treatment[grep("AC", vis.data$plant_id)] <- 16
vis.data$treatment[grep("AD", vis.data$plant_id)] <- 33
vis.data$treatment[grep("AE", vis.data$plant_id)] <- 66

# Add plant genotype column coded in barcodes
vis.data$genotype <- NA
vis.data$genotype[grep("p1", vis.data$plant_id)] <- 'A10'
vis.data$genotype[grep("p2", vis.data$plant_id)] <- 'B100'
vis.data$genotype[grep("r1", vis.data$plant_id)] <- 'R20'
vis.data$genotype[grep("r2", vis.data$plant_id)] <- 'R70'
vis.data$genotype[grep("r3", vis.data$plant_id)] <- 'R98'
vis.data$genotype[grep("r4", vis.data$plant_id)] <- 'R102'
vis.data$genotype[grep("r5", vis.data$plant_id)] <- 'R128'
vis.data$genotype[grep("r6", vis.data$plant_id)] <- 'R133'
vis.data$genotype[grep("r7", vis.data$plant_id)] <- 'R161'
vis.data$genotype[grep("r8", vis.data$plant_id)] <- 'R187'

# Add genotype x treatment group column
vis.data$group = paste(vis.data$genotype,'-',vis.data$treatment,sep='')

# Add calendar-time data column using the Unix-time data
vis.data$date = as.POSIXct(vis.data$datetime, origin = "1970-01-01")

# Calculate days after planting from planting data
vis.data$dap = as.numeric(vis.data$date - planting_date)

# Convert VIS camera zoom units. LemnaTec VIS camera zoom units range from 1 to 6000, which correspond to 1 to 6X zoom
zoom.lm = lm(zoom.camera ~ zoom, data=data.frame(zoom=c(1,6000), zoom.camera=c(1,6)))

# VIS zoom correction
# Download data for a reference object imaged at different zoom levels.
if (!file.exists('zoom_calibration_data.txt')) {
  download.file('http://files.figshare.com/2084101/zoom_calibration_data.txt',
                'zoom_calibration_data.txt')
}
z.data = read.table(file="zoom_calibration_data.txt", sep="\t", header=TRUE)

# Calculate px per cm
z.data$px_cm = z.data$length_px / z.data$length_cm

# Convert LemnaTec zoom units to camera zoom units
z.data$zoom.camera = predict(object = zoom.lm, newdata=z.data)
vis.data$zoom = vis.data$sv_zoom
vis.data$sv.zoom.camera = predict(object = zoom.lm, newdata=vis.data)
vis.data$zoom = vis.data$tv_zoom
vis.data$tv.zoom.camera = predict(object = zoom.lm, newdata=vis.data)

# Non-linear (exponential) model for area zoom correction
area.coef = coef(nls(log(rel_area) ~ log(a * exp(b * zoom.camera)),
                     z.data, start = c(a = 1, b = 0.01)))
area.coef = data.frame(a=area.coef[1], b=area.coef[2])
area.nls = nls(rel_area ~ a * exp(b * zoom.camera),
               data = z.data, start=c(a=area.coef$a, b=area.coef$b))

# Non-linear (polynomial) model for length zoom correction
len.poly = lm(px_cm ~ zoom.camera + I(zoom.camera^2),
              data=z.data[z.data$camera == 'VIS SV',])
              
# Create zoom-corrected VIS data frame
vis.data.zoom = vis.data[,c('plant_id', 'datetime', 'treatment', 'genotype', 'group', 'date', 'dap', 'solidity', 'outlier')]
vis.data$zoom.camera = vis.data$sv.zoom.camera
vis.data$sv_rel_area = predict(object = area.nls, newdata = vis.data)
vis.data$zoom.camera = vis.data$tv.zoom.camera
vis.data$tv_rel_area = predict(object = area.nls, newdata = vis.data)

# Calculate total zoom-corrected side-view and top-view area
vis.data.zoom$sv_area = (vis.data$sv0_area / vis.data$sv_rel_area) + (vis.data$sv90_area / vis.data$sv_rel_area) + (vis.data$sv180_area / vis.data$sv_rel_area) + (vis.data$sv270_area / vis.data$sv_rel_area)
vis.data.zoom$tv_area = vis.data$tv_area / vis.data$tv_rel_area

# Calculate zoom-corrected lengths
vis.data$zoom.camera = vis.data$sv.zoom.camera
vis.data$px_cm = predict(object = len.poly, newdata=vis.data)
vis.data.zoom$extent_x = vis.data$extent_x / vis.data$px_cm
vis.data.zoom$extent_y = vis.data$extent_y / vis.data$px_cm
vis.data.zoom$height_above_bound = vis.data$height_above_bound / vis.data$px_cm
```

## Model fresh-weight biomass from image data for Setaria

Download data manually measured plant biomass data set (n = 41).

```r
if (!file.exists('manual_biomass_samples.csv')) {
  download.file('http://files.figshare.com/2084103/manual_biomass_samples.csv',
                'manual_biomass_samples.csv')
}
```

Read the CSV file

```r
manual.st.data = read.table(file='manual_biomass_samples.csv', sep=",", header=TRUE, stringsAsFactors=FALSE)
```

Get data from the VIS data for each manual biomass sample
```r
st.data = merge(manual.st.data, vis.data.zoom, by = c('plant_id', 'datetime'))
```

A full model for fresh-weight biomass. Includes side-view area, top-view area and height.
```r
fw.full = lm(fresh_weight ~ sv_area * tv_area * height_above_bound, st.data)
```

Step-wise model selection with AIC.
```r
fw.step = stepAIC(fw.full, direction="both")
summary(fw.step)
```

AIC model
```r
fw.aic = lm(fresh_weight ~ sv_area + tv_area + height_above_bound +
              sv_area*height_above_bound, st.data)
summary(fw.aic)
```

The AIC model contains tv_area and height which does not have a significant coefficient, test dropping.
```r
fw.red = lm(fresh_weight ~ sv_area, st.data)
summary(fw.red)
```

Goodness of fit.
```r
anova(fw.aic, fw.red)
```

Side-view area model.
```r
sv.model = lm(fresh_weight ~ sv_area, st.data)
summary(sv.model)
```

Plot SV model
```r
sv.model.plot = ggplot(st.data,aes(x=sv_area/1e5, y=fresh_weight)) +
                       geom_smooth(method="lm", color="black", formula = y ~ x) +
                       geom_point(size=2.5) +
                       scale_x_continuous("Shoot and leaf area (x10^5 px)") +
                       scale_y_continuous("Fresh-weight biomass (g)") +
                       theme_bw() +
                       theme(axis.title.x=element_text(face="bold"),
                             axis.title.y=element_text(face="bold"))
print(sv.model.plot)
```

##Introduction to Scratch

**More here from Meter**

##Tech Trunk Discussion Notes

**Moderated by Terry**

**Notes:**

##Module planning notes

**Moderated by Terry**

**Notes:**
