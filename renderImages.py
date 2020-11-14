import bpy
import json
import os
import subprocess
import sys
import random

python = "../blender-2.83/blender-2.83.0-linux64/2.83/python/bin/python3.7m"

subprocess.call([python, '-m', 'ensurepip'])
subprocess.call([python, '-m', 'pip', 'install', 'boto3', '--user'])

import boto3

# Without this, the rendering will finish after a few days. Should be False.
bpy.context.scene.cycles.use_square_samples = False

data = json.load(open('data.json'))

imagesToRender = data['options']['images_to_render']

filepath = ['/home/blender-git/render-output/',
            './renders/']

# Download dependencies
#subprocess.Popen('wget', '--no-check-certificate', 'https://www.dropbox.com/sh/fpu6gcfoz68fwm7/AADZDBWeLTSdiBKJrURVD743a?dl=1')


def main():
    # Set render resolution
    scene = bpy.context.scene
    furniture = bpy.data.collections['Furniture']
    lights = bpy.data.collections['Lights']
    groundtruth = bpy.data.collections['GroundTruth']

    base_light_brightness = 100
    base_world_lighting = 1
    rendered_images = 0

    # Render 5 different distributions of furniture ranging from none to all.
    furniture_level = [0, 5, 9, 13, 18]

    # Set light brightness by multiplying base_light_brightness by the percentages.
    light_level = [0.6, 1, 1.4, 1.8, 2]

    scene.render.resolution_x = 1920/2
    scene.render.resolution_y = 1080/2

    if not os.path.exists('./renders/'):
        os.mkdir('./renders/')

    if data['authority']['render_all']:
        print("Rendering all images.")

        # Set camera object.
        camera = bpy.data.objects['Camera']

        for i in range(imagesToRender):

            # Cycle through random furniture distributions.
            for f in furniture_level:
                # Use the random module to select random furniture in the room.
                if (f != 0):
                    selected_furniture = [random.randrange(0, f)]

                # Hide all furniture.
                for i in bpy.data.collections['Furniture'].objects:
                    if i.name.startswith('furniture.'):
                        i.hide_render = True

                # Show only desired furniture.
                for i in range(f):
                    #if i.name.startswith('furniture.'):
                    furniture[i].hide_render = False

                # Cycle through different levels of brightness.
                for l in light_level:

                    # Set light brightness for world background.
                    bpy.data.worlds['World'].node_tree.nodes['Background'].inputs[1].default_value = base_world_lighting * l

                    # Set light brightness for all light objects in scene.
                    for i in lights.objects:
                        # Ensure only objects with prefix in collection are affected.
                        if i.name.startswith('light.'):
                            i.data.energy = base_light_brightness * l

                    # Image
                    image = "image.{}.furniture.{}.light.{}".format(str(rendered_images), f, str(l*100))

                    # Set Camera desired degree.
                    desired_degree = camera.rotation_euler.z + 360 / imagesToRender

                    # Rotate camera by desired degree.
                    camera.rotation_euler.z = desired_degree

                    # Set render file location.
                    bpy.context.scene.render.filepath = (filepath[1] + image)

                    # Begin rendering the image.
                    bpy.ops.render.render(write_still=True)

                    rendered_images += 1

                    # Upload latest render.
                    subprocess.call(['aws', 's3','cp', filepath[1] + image + '.png', 's3://{}/{}.png'.format(data['authority']['s3'], image)])


    else:
        print ("Rendering single image.")

        # Set render file location.
        bpy.context.scene.render.filepath = (filepath[1] + 'image.png')

        # Begin rendering the image.
        bpy.ops.render.render(write_still=True)

        # Upload latest render.
        #subprocess.call(['aws', 's3','cp',filepath[1] + 'image.png', 's3://{}/image.png'.format(data['authority']['s3'])])

    bpy.ops.wm.quit_blender()


if __name__ == "__main__":
    main()
