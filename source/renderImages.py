import json
import os
import sys
import subprocess

data = json.load(open('data.json'))


def main():
    if data['authority']['render_all']:
        print("Rendering all images.")
    else:
        print ("Rendering single image.")


if __name__ == "__main__":
    main()
