
import sys
import json
import os

class Encoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

class Settings:
    def __init(self):
        self.os = sys.platform
        self.use_aws = False
        self.project_path = os.getcwd()
        self.render_path = os.getcwd() + '\\renders\\'
        self.source_path = os.getcwd() + '\\source\\'
    
    def load(self):
        filename = os.getcwd() + '\\source\\' + 'settings.json'
        if os.path.isfile(filename):
            filename = open(os.getcwd() + '\\source\\' + 'settings.json', 'r')
            self.__dict__ = json.load(filename)
        else:
            filename = os.getcwd() + '\\source\\' + 'settings.json'
            print ("settings.json not found.")
            print ("Generating new settings file...")
            open(filename, 'w+')
        return self

    def save(self):
        Encoder().encode(self)
        filename = os.getcwd() + '\\source\\' + 'settings.json'
        json.dump(self, open(filename,'w+'), indent=4, cls=Encoder)
        return self

s = Settings().save().load()
