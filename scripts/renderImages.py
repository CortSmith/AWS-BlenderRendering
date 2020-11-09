# Author: Cort Smith

import os
import sys
import bpy
import time
import toml
import uuid
import random


def load_config(path):
    """Loads a dictionary from configuration file.

    Args:
        path: the path to load the configuration from.

    Returns:
        The configuration dictionary loaded from the file.
    """
    return toml.load(path)


config = load_config('config.toml')
settings = config['Settings']
render = config['Render']

random.seed(time.time() % int(settings['furniture_levels'][4]))

def main():
    session_id = str(uuid.uuid4())[:8]
    config['Render']['session_id'] = uuid

    # Set render resolution
    scene = bpy.context.scene
    objects = bpy.data.objects
    rotation_degree = 360 / settings['max_renders']
    camera = objects['Camera']

    render['continue_render'] = True

    scene.render.resolution_x = settings['render_resolution'][0]
    scene.render.resolution_y = settings['render_resolution'][1]

    if render['render']:
        if render['full_render']:
            pass
            for f in settings['furniture_levels']:
                for l in settings['lighting_levels']:
                    pass
                # f
            # else
        # if
        else:
            for i in range(settings['max_renders']):
                desired_degree = camera.rotation_euler.z + rotation_degree
                # {C:/Path/To/Dir/../renders/} {session_id} / {image}.{images_rendered.png}
                scene.render.filepath = "{}/{}/{}.{}.png".format(os.getcwd() + '../renders/',
                                                                 session_id, 'image', str(i))
                if not render['session_completed']:
                    i = int(render['rendered_images'])

                config['Render']['rendered_images'] = i
                bpy.ops.render.render(write_still=True)
                # i
            # else
        # if

    bpy.ops.wm.quit_blender()
    sys.exit()
    # Main()


if __name__ == '__main__':
    main()

    """
    if Settings['render_all']:
        print("Rendering all images.")
        
        # Set camera object.
        camera = objects['Camera.001']
        
        for i in range(totalImagesRendered):

            # Set Camera desired degree.
            desired_degree = camera.rotation_euler.z + rotation_degree
            
            # Rotate camera by desired degree.
            camera.rotation_euler.z = desired_degree
            
            # Set render file location.
            bpy.context.scene.render.filepath = "{}/{}/{}.{}.{}".format(data['render_path'], fileUUID, 'image', str(fileUUID),str(i))
            
            if render_state['continue_render'] and i == 0:
                i = int (render_state['images_rendered'])
            
            render_state['images_rendered'] = i

            # Begin rendering the image.
            bpy.ops.render.render(write_still=True)
            
            render_state['images_rendered'] = i
            json.dump(render_state, open('render_state.json','w'))
        
    else:
        print ("Rendering single image.")
        
        # Set render file location.
        bpy.context.scene.render.filepath = (data['render_path'])
    
        # Begin rendering the image.
        bpy.ops.render.render(write_still=True)
    
    render_state['continue_render'] = False
    bpy.ops.wm.quit_blender()
"""
