# Image Analysis Session: Working with GitHub and PlantCV

For this session we are going to do a real experiment. We will use image analysis to measure the size of seeds that you took pictures of with the Raspberry Pi cameras.

# Outline
1. Use git to clone your own copy of PlantCV
3. Image analysis with PlantCV on Jupyter
4. Analyze processed phenotype data in R on Jupyter

# Getting software from GitHub

Git is a code (text) versioning program that is used to keep track of changes between updates to code repositories. GitHub is a company that developed an online repository and social code development environment built around git. Using git with GitHub (or alternatives) is important for open science. Making your code available means it is available to other scientists, makes it less likely that accidental errors go unnoticed, and is a transparent disclosure of the methods you used. Additionally, Versioning programs like git also make it easier to collaborate on coding projects.   

## Clone the PlantCV repository

First, make sure you are home:

```
cd ~
```

Then clone PlantCV to your home folder:

```
git clone https://github.com/danforthcenter/plantcv.git
```

# Process images with PlantCV

[PlantCV](http://plantcv.danforthcenter.org/) is software we wrote at the Danforth Center to extract biologically meaningful information from images of plants. Go to [here](http://plantcv.danforthcenter.org/pages/documentation/function_docs/vis_tutorial.html) for detailed instructions.

We are going to run PlantCV and the phenotype analyses on our Jupyter Notebook server. This repository includes Jupyter Notebook files for PlantCV and R to use to build your own notebooks.