# Author: Cort Smith

import os
import sys
import subprocess


def decompress(name, filetype = '.rar', source = '../source/', dest = '../source'):
    if filetype == '.rar':
        subprocess.call(['unrar', 'x', source + name + '.rar', dest])
    if filetype == '.tar.gz':
        subprocess.call(['tar', '-zxvf', source + name + '.tar.gz', '', dest])


def download(name, url, flags, dest = '../source/'):

    if not os.path.isdir(dest):
        os.mkdir(dest)

    if not os.path.isdir(dest + name):
        dl = subprocess.call(['wget', url, flags, '-P', dest])


URL = 'https://filedn.com/lY4OilwSUTkYLthqPG90arh/AWSBR.rar'
Flags = '--show-progress'
Path = '../source/AWSBR.rar'
Name = 'AWSBR'

download(Name, URL, Path)
decompress(Name)




