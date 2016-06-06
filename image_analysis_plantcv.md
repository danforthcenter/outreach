# Image Analysis Session: Working with GitHub, Figshare and PlantCV

In the morning you saw the Danforth Center phenotyping facility. In this session we use the Plant Computer Vision (PlantCV) software to analyze images from the phenotyping system. We will also discuss using GitHub, Figshare and some data analysis in R.

# Outline
1. Use git to clone your own copy of the workshop materials
2. Install a program on the Raspberry Pi to view rendered Markdown files
3. Image analysis with PlantCV
4. Analyze processed phenotype data in R

# Getting software from GitHub

Git is a code (text) versioning program that is used to keep track of changes between updates to code repositories. GitHub is a company that developed an online repository and social code development environment built around git. Using git with GitHub (or alternatives) is important for open science. Making your code available means it is available to other scientists, makes it less likely that accidental errors go unnoticed, and is a transparent disclosure of the methods you used. Additionally, Versioning programs like git also make it easier to collaborate on coding projects.   

## Clone the workshop materials

On the command line, type:

```
git clone https://github.com/danforthcenter/nsf_reu_workshop.git
```

# Install software on the Raspberry Pi

The workshop materials are written in Markdown. Markdown is a simplified syntax system for applying formatting rules to text (see [here](https://github.com/raspberrypilearning/creating-resources/blob/master/markdown.md) for a guide to writing Markdown). The Markdown files in the workshop repository are text files that can be opened with any text editor, but to view the file with formatting we need a program that can display rendered Markdown. There are various ways to install software with Linux-based operating systems. Generally the easiest method is to use the operating system package management program. On Debian-based systems, including Raspbian, the system package manager is called apt-get.

## Install the Markdown editor/viewer ReText

On the command line, type:

```
sudo apt-get install retext
```

# Process images with PlantCV

[PlantCV](http://plantcv.danforthcenter.org/) is software we wrote at the Danforth Center to extract biologically meaningful information from images of plants. Go to [here](http://plantcv.danforthcenter.org/pages/documentation/function_docs/vis_tutorial.html) for detailed instructions.

Pick an image and look at the name to determine which script to run most scripts are in dev (see example below) type:

```
path_to_script –i path_to_image –o destination_folder_for_output_images –D
```

For example:

```
/home/pi/plantcv/scripts/dev/vis_sv_z2500_L2_e82.py -i /home/pi/nsf_reu_workshop/sample_images/brachypodium/VIS_SV_0_z2500_h2_g0_e82_300296\ copy.png -o . -D
```

# Use R to analyze phenotyping data

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

Read the data from the CSV file.

```r
vis.data = read.table(file="vis_snapshots_nocorrect.csv", sep=",", header=TRUE)
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
