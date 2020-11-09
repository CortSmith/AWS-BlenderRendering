import json
import os
import sys
import uuid



class pyObjectEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

class pyObject:
    def __init__(self):
        self.x = None
        self.y = None
        self.resolution = [1920,1080]
        self.uuid = str(uuid.uuid4())[:8]
    
    def default(self, o):
        return o.__dict__

    def save_configuration(self):
        json.dump(self.__dict__, os.getcwd() + '/pyObject.json')


o = pyObject()

print (json.JSONEncoder().encode(o.__dict__))

print ("Encode o Object into JSON formatted Data using custom JSONEncoder")
encodedObject = json.dumps(o.__dict__, indent=4, cls=json.JSONEncoder)
#oEncoderData = json.dumps(o, indent=4, cls=pyObjectEncoder)
print (encodedObject)

print ("Decode JSON formatted Data")
DecodedObject = json.loads(encodedObject)
#oEncoder = json.loads(oEncoderData)
print (DecodedObject)

