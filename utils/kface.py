import os
import shutil

# if __name__ == '__main__':
# root_dir = './High_Resolution/'
root_dir = './19062421/'
# root_dir = '/Users/letsg/Dropbox/여행'


for pwd, dirs, files in os.walk(root_dir):
    print('# pwd:', pwd)
    print('# dir:', dirs)
    print('# files:', files)

    # if len(dirs) > 0:
    #     for dir_name in dirs:
    #         print('dir:' + dir_name)

    # if len(files) > 0:
    #     for file_name in files:
    #         print('file:' + file_name)