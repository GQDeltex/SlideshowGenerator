# SlideshowGenerator
A Slideshow Generator based on reveal-md (which is based on revealjs) which generates Slideshows from a structure.yml and prewritten slides out of a Slides directory.

## Prerequisites:
At this point in time there is no executable binary version available (though this is considered for the future), so you still need some other programs to run the slideshow generator:
- [NPM (from NodeJS)](https://nodejs.org/en/download/)
- [Python (2.7)](https://www.python.org/downloads/)

## Installation:
```
git clone https://github.com/GQDeltex/SlideshowGenerator.git
# or just download and extract the zip
cd SlideshowGenerator
npm install
```
## Test the Installation:
```
python generate_slides.py
```
In terminal:
```
Path to Project Folder: test_project
Path to Slides Folder: Slides
# [Ctrl-C] to exit
```

This should open your Webbrowser and you should see a test slideshow

## Using the Tool:
You just make a project directory and put a 'structure.yml' file in there. In that file you write the structure of your presentation (oh, who would've thought of that?). Something like in the [template.yml](template.yml).

For your prewritten Slides, you can use the already existing 'Slides' directory or just define your own (which you have to type into the program or specify in [generate_slides.py](generate_slides.py)). In this Folder you write the slide content in Markdown (see 'Slides/Some other Slide.md' as example) the Syntax is not that Hard, have a look at [reveal-md](http://webpro.github.io/reveal-md/) for further reading. 