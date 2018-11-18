import SlideGenerator
from subprocess import call
import os

if __name__ == '__main__':
    # If you specify you path here, it will be used every time without asking fist (useful for longer sessions)
    project_path = ''
    # You can also just specify the slides_path if the folder stays static
    slides_path = ''
    # Or if nothing is specified, just ask :-)
    if not project_path: project_path = str(raw_input('Path to Project Folder: '))
    if not slides_path: slides_path = str(raw_input('Path to Slides Folder: '))
    SG = SlideGenerator.SlideGenerator(project_path, slides_path)
    SG.read_template()
    SG.process_template()
    SG.write_slideshow()
    path_to_reveal_md = os.path.join(os.getcwd(), 'node_modules/.bin/reveal-md')
    print(path_to_reveal_md)
    call([path_to_reveal_md, './slides.md'], cwd=project_path)