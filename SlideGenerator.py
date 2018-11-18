import os
import codecs
import yaml
from shutil import copyfile

class SlideGenerator (object):
    def __init__(self, project_path='./', slides_path='./Slides'):
        self.project_path = project_path
        self.slides_path = slides_path
        if not os.path.isdir(self.project_path):
            raise IOError('Couldn\'t open the Project Folder (maybe it doesn\'t exist)')
        if not os.path.isdir(self.slides_path):
            raise IOError('Couldn\'t open the Slides Folder (maybe it doesn\'t exist)')
    
    def read_template(self, filename='structure.yml'):
        self.structure_file_path = os.path.join(self.project_path, filename)
        if not os.path.isfile(self.structure_file_path):
            raise IOError('Couldn\'t open the Structure File (maybe it doesn\'t exist)')
        with codecs.open(self.structure_file_path, 'r', 'utf-8-sig') as infile:
            try:
                self.structure = yaml.load(infile)
            except yaml.YAMLError as exc:
                raise
        if not self.structure:
            raise ValueError('No content in the Structure File!')
    
    def process_template(self):
        self.slideshow = []
        is_title = False
        is_agenda = False
        if 'title' in self.structure:
            if self.structure['title'] != None:
                self._process_title()
                is_title = True
        if 'agenda' in self.structure:
            if self.structure['agenda'] != None:
                for slide in self.structure['agenda']:
                    if is_title or is_agenda: self.slideshow.append('\n---\n\n')
                    self._process_slide(slide)
                    is_agenda = True
        if 'endcard' in self.structure:
            if self.structure['endcard'] != None:
                if is_title or is_agenda: self.slideshow.append('\n---\n\n')
                self._process_endcard()

    def write_slideshow(self, filename='slides.md'):
        self.slideshow_file_path = os.path.join(self.project_path, filename)
        with codecs.open(self.slideshow_file_path, 'w', 'utf-8-sig') as outfile:
            for line in self.slideshow:
                outfile.write(line)
    
    def _process_title(self):
        num_of_titles = len(self.structure['title'])
        start = 0
        if num_of_titles > 1:
            title = self.structure['title'][0]
            self.slideshow.append('## ' + title + '\n')
            start = 1
        for title in self.structure['title'][start:]:
            self.slideshow.append('### ' + title + '\n')
    
    def _process_slide(self, slide):
        slide_location = os.path.join(self.slides_path, slide + '.md')
        if slide.startswith('CUSTOM '):
            text = slide.replace('CUSTOM ', '', 1)
            self.slideshow.append(text + '\n')
        elif not os.path.isfile(slide_location):
            raise IOError('Couldn\'t read Template for %s' % slide)
        else:
            with codecs.open(slide_location, 'r', 'utf-8-sig') as slide_file:
                self.slideshow.extend(slide_file.readlines())
                self.slideshow.append('\n')
    
    def _process_endcard(self):
        num_of_titles = len(self.structure['endcard'])
        start = 0
        if num_of_titles > 1:
            title = self.structure['endcard'][0]
            self.slideshow.append('## ' + title + '\n')
            start = 1
        for title in self.structure['endcard'][start:]:
            self.slideshow.append('### ' + title + '\n')

