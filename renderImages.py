import bpy
import json
import os
import subprocess
import sys

subprocess.call(['python', '-m', 'ensurepip'])
subprocess.call(['python', '-m', 'pip', 'install', 'boto3'])

import boto3

data = json.load(open('data.json'))

imagesToRender = data['options']['images_to_render']

filepath = ['/home/blender-git/render-output/',
            './renders/']

# Download dependencies
# subprocess.Popen('wget', '--no-check-certificate', 'https://www.dropbox.com/sh/fpu6gcfoz68fwm7/AADZDBWeLTSdiBKJrURVD743a?dl=1')


def main():
    # Set render resolution
    scene = bpy.context.scene
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    
    if not os.path.exists('./renders/'):
        os.mkdir('./renders/')
    
    if data['authority']['render_all']:
        print("Rendering all images.")
        
        # Set camera object.
        camera = bpy.data.objects['Camera.001']
        
        for i in range(imagesToRender):
            
            # Set Camera desired degree.
            desired_degree = camera.rotation_euler.z + 180 / imagesToRender
            
            # Rotate camera by desired degree.
            camera.rotation_euler.z = desired_degree
            
            # Set render file location.
            bpy.context.scene.render.filepath = (filepath[1] + 'image.' + str(i))
        
            # Begin rendering the image.
            bpy.ops.render.render(write_still=True)

            # Upload latest render.
            subprocess.call(['aws', 's3','cp',filepath[1] + 'image.' + str(i) + '.png'])

        
    else:
        print ("Rendering single image.")
        
        # Set render file location.
        bpy.context.scene.render.filepath = (filepath[1] + 'image.png')
    
        # Begin rendering the image.
        bpy.ops.render.render(write_still=True)

        # Upload latest render.
        subprocess.call(['aws', 's3','cp',filepath[1] + 'image.png'])
    
    bpy.ops.wm.quit_blender()


if __name__ == "__main__":
    main()
