from PIL import Image
import os, sys

path = "/mnt/c/users/nanda gopal/desktop/tensorflow2.0/data/"
dirs = os.listdir( path )
dest= "/mnt/c/users/nanda gopal/desktop/tensorflow2.0/data1/"
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            if im.mode != 'RGB':
                im = im.convert('RGB')

            imResize = im.resize((250,250), Image.ANTIALIAS)
            os.chdir("/mnt/c/users/nanda gopal/desktop/tensorflow2.0/data1")
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()