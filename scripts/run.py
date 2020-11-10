# Author: Cort Smith

import subprocess

subprocess.call(['blender', '--background', '../source/AWSBR/.blend/2StorySampleRender.blend',
                            '--python', 'renderImages.py'])