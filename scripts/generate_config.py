# Author: Cort Smith

config = '''
# @use_aws - Enable aws services, notably EC2 and S3.
[AWS]
use_aws = false
username = ""
password = ""
aws_bucket_id = ""

# @session_id - Unique session identifier using an 8-digit uuid.
# @session_complete - Session completed without interruption.
# @rendered_images - Number of images successfully rendered.
# @furniture_level - Last furniture level achieved before termination.
# @lighting_level - Last lighting level achieved before termination.
[Render]
session_id = ""
session_complete = true
rendered_images = 0
furniture_level = 0
lighting_level = 0

# @render - Enable image rendering.
# @render_resolution - Rendered Image resolution.
# @full_render - Enable rendering of furniture and lighting levels - O(n)
# @max_renders - Number of images to render.
#              - If full_render, will render 25 images per iteration.
# @furniture_levels - [0%, 25%, 50%, 75%, 100%] amount of furniture to display per iteration.
#                   - Adjust values as whole numbers, not percentages.
# @lighting_levels - [60%, 85%, 100%, 115%, 140%] brightness of lights in the scene.
#                  - These values should be decimals, not percentages.
# @camera - Name of camera object being used. Defaults to 'Camera'
# @labels - Naming convention of objects in scene.
#         - These names are used by the script to identify objects in the scene.
# @collections - Naming convention of collects in the scene.
#              - These names are used by the script to identify the collections in the scene.
[Settings]
render = true
render_resolution = [ "500", "500",]
full_render = false
max_renders = 1
furniture_levels = []
lighting_levels = []
camera = "Camera"
labels = [ "furniture", "light", "GT", "cp.", "camera",]
collections = [ "Furniture", "Lights", "GroundTruth", "CameraPositions",]

'''

with open('../source/config.toml', 'w+') as f:
    f.write(config)
