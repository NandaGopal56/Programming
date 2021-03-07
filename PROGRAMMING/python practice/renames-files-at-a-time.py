import os
#path to folder
path = '/mnt/c/users/nanda gopal/desktop/tensorflow2.0/data1'
files = os.listdir(path)

for index, file in enumerate(files):
   os.rename(os.path.join(path, file), os.path.join(path, ''.join(['image'+str(index), '.png'])))