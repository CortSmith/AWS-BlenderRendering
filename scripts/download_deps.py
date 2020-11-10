# Author: Cort Smith

import os
import sys
import subprocess


def decompress(name, filetype = '.rar', source = '../source/', dest = '../source/'):
    if filetype == '.rar':
        if not os.path.isdir(source + name):
            subprocess.call(['unrar', 'x', source + name + '.rar', dest])
    if filetype == '.tar.gz':
        if not os.path.isdir(source + name):
            subprocess.call(['tar', '-zxvf', source + name + '.tar.gz', '', dest])
    else:
        print ("Path exists.")


def download(name, url, flags, dest = '../source/'):

    if not os.path.isdir(dest):
        os.mkdir(dest)

    if not os.path.isdir(dest + name):
        if not os.path.isfile(dest + name + '*'):
            dl = subprocess.call(['wget', url, flags, '-P', dest])
    else:
        print ("File exists.")


URL = 'https://filedn.com/lY4OilwSUTkYLthqPG90arh/AWSBR.rar'
Flags = '--show-progress'
Path = '../source/AWSBR.rar'
Name = 'AWSBR'

download(Name, URL, Path)
decompress(Name)




