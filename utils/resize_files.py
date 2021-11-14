import os 
import glob
from PIL import Image

files = glob.glob('C:\dev\KFG\Korean\AFAD_gathered/*')

for f in files:
    title, ext = os.path.splitext(f)
    if ext in ['.jpg']:
        img = Image.open(f)
        img_resize = img.resize((128, 128))
        img_resize.save(title+ext)