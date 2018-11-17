# SlideshowGenerator
A Slideshow Generator based on reveal-md (which is based on revealjs) which generates Slideshows from a structure.yml and prewritten slides out of a Slides directory.

## Installation:
```
git clone https://github.com/GQDeltex/SlideshowGenerator.git
cd SlideshowGenerator
npm install
```
## Test the Installation:
```
python generate_slides.py  #Type 'test_project' as the Path (and yes I know there is a Slide missing)
./node_modules/.bin/reveal-md ./test_project/slides.md
```
