import os
import codecs
import yaml
from shutil import copyfile

project_path = str(raw_input("Path to Project Folder: "))
print("")
if not os.path.isdir(project_path):
    print("[ERROR] The given project Path doestn't exist")
    exit()
structure_file_path = os.path.join(project_path, 'structure.yml')
slide_file_path = os.path.join(project_path, 'slides.md')
slides_location = './Slides/'
missing_slides = []

if os.path.isfile(structure_file_path):
    print("[INFO] Structure File exists, perfect!")
else:
    copyfile('./template.yaml', structure_file_path)
    print("[ALERT] Edit your structure first ('structure.yml' in project folder)")
    exit()

with codecs.open(structure_file_path, 'r', 'utf-8-sig') as infile:
    try:
        structure = yaml.load(infile)
        print(structure)
    except yaml.YAMLError as exc:
        print(exc)
        exit()
if not structure:
    exit()
print("[INFO] Successfully read the Structure File!")

with codecs.open(slide_file_path, 'w', 'utf-8-sig') as outfile:
    print("[INFO] Writing Slides to file\n")
    for title in structure['title']:
        print("[INFO] TITLE: %s" % title)
        outfile.write('## ' + title + '\n')
    outfile.write('\n---\n\n')
    print("\n")
    for slide in structure['agenda']:
        if slide.startswith("CUSTOM "):
            text = slide.replace("CUSTOM ", "")
            print("[INFO] Detected Custom Slide: %s" % text)
            outfile.write(text + "\n")
            outfile.write("\n---\n\n")
            continue
        if not os.path.isfile(os.path.join(slides_location, slide + '.md')):
            print("[ERROR], the slide '%s' doestn't exist in your slides directory (%s)" % (slide, slides_location))
            missing_slides.append(slide)
            continue
        with codecs.open(os.path.join(slides_location, slide + '.md'), 'r', 'utf-8-sig') as slide_file:
            print("[INFO] SLIDE: %s" % slide)
            slide_file_contents = slide_file.read()
            outfile.write(slide_file_contents)
            outfile.write('\n---\n\n')
    print("\n")
    for title in structure['endcard']:
        print("[INFO] ENDCARD: %s" % title)
        outfile.write('## ' + title + '\n')

print("\n\n[ALERT] Some Slides are missing:")
for slide in missing_slides:
    print("- " + slide)