# Author: Cort Smith
# Project Name: AWS-BlenderRendering
# Project Description: Automated Rendering with Blender and Python

import os
import sys
import json
import uuid




class Encoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

class State:
    def __init__(self):
        self.images_rendered = 0
        self._continue = False
        self.uuid = ""

class Renderer:
    def __init__(self):
        # String => Unique render session id
        self.uuid = str(uuid.uuid4())[:8]
        
        # Boolean => Allow rendering of single image for testing or all images.
        # Options: 0 <disable rendering> | 1 <render one image> | 2 <render all images>
        self.render = 1
        
        # Boolean => Identifies which os is currently running this script.
        self.os = sys.platform
        
        # Render State
        self.state = State()
        
        # Use aws to render images with blender.
        self.use_aws = False
        
        # String => System paths to directories
        self.project_path = os.getcwd()
        self.render_path = self.project_path + '\\renders\\'
        self.source_path = self.project_path + '\\source\\'
        
        self.state._continue = False
        self.state.images_rendered = 0
        self.state.uuid = self.uuid
        
        
    def build_dependencies(self):
        if not os.path.exists(self.render_path):
            os.mkdir(self.render_path)
        
        if not os.path.exists(self.source_path + 'renderer.json'):
            # Make directory if it doesn't exist.
            if (os.path.isdir(self.source_path):
                    os.mkdir(self.source_path)

            # Make directory if it doesn't exist.
            if (os.path.isdir(self.render_path):
                os.mkdir(self.render_path)
            
            self.save_configuration()
    
    def save_configuration(self):
        Encoder().encode(self)
        with open(self.source_path + 'renderer.json', 'w+') as config:
            json.dump(self, config, indent=4, cls=Encoder)
        
        
    def load_configuration(self):
        with open(self.source_path + 'renderer.json', 'r') as config:
            temp = json.load(config)
            if (temp['_continue']):
                self.__dict__ = json.load(config)

    def setup(self):
        self.build_dependencies()
        self.load_configuration_files()




def main():
    r = Renderer()
    r.build_dependencies()
    r.save_configuration()


if __name__ == "__main__":
    main()



