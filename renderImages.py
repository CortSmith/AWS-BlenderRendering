
import bpy
import json
import os
import sys
import subprocess


data = json.load(open('data.json'))

totalImagesRendered = 3

filepath = ['/home/blender-git/render-output/',
            './renders/']

# Download dependencies
subprocess.Popen('wget', '--no-check-certificate', 'https://www.dropbox.com/sh/fpu6gcfoz68fwm7/AADZDBWeLTSdiBKJrURVD743a?dl=1')


def main():
    # Set render resolution
    scene = bpy.context.scene
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    
    os.mkdir('./renders/')
    
    if data['authority']['render_all']:
        print("Rendering all images.")
        
        # Set camera object.
        camera = bpy.data.objects['Camera.001']
        
        for i in range(totalImagesRendered):
            
            # Set Camera desired degree.
            desired_degree = camera.rotation_euler.z + 180 / totalImagesRendered
            
            # Rotate camera by desired degree.
            camera.rotation_euler.z = camera.desired_degree
            
            # Set render file location.
            bpy.context.scene.render.filepath = (filepath[1] + 'image.' + i)
        
            # Begin rendering the image.
            bpy.ops.render.render(write_still=True)
        
    else:
        print ("Rendering single image.")
        
        # Set render file location.
        bpy.context.scene.render.filepath = ('/home/blender-git/render-output/image.test')
    
        # Begin rendering the image.
        bpy.ops.render.render(write_still=True)
    
    bpy.ops.wm.quit_blender()


if __name__ == "__main__":
    main()
