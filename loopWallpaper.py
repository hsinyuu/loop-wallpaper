import os
import time

INTERVAL = 10 #secs
IMG_EXTENSIONS = ('.jpg', '.jpeg')

def isImage(file_name):
    fname, fext = os.path.splitext(file_name)
    return fext in IMG_EXTENSIONS

def setWallpaper(img_path):
    """Set the wallpaper of the system using oascript"""
    cmd = filepath = "osascript -e 'tell application \"Finder\" " \
                        + "to set desktop picture to POSIX file \"" \
                        + img_path +"\"'"
    os.system(cmd)

def loopWallpaper(base_path):
    """Loop through and set wallpaper to each image in the base_path
    per INTERVAL seconds"""
    for img_file in os.listdir(base_path):
        if not isImage(img_file):
            continue
        img_path = base_path + img_file
        print('Set wallpaper to {}'.format(img_path))
        setWallpaper(img_path)
        time.sleep(INTERVAL)

if __name__ == '__main__':
    loopWallpaper('/Users/yu/Documents/wallpaper/')
