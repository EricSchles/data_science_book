import os
import glob
from PIL import Image

def changeType(img):
    im = Image.open(img)
    first = img.split(".")[0]
    im.save(first+".png")

def resize(img):
    im = Image.open(img).convert('LA')
    w,h = im.size
    newIm = im.resize((30,30))
    first = img.split(".")[0]
    newIm.save(first+"copy.png")

images = glob.glob("*.png")
for image in images:
    resize(image)
# images = glob.glob("*.jpg")
# for image in images:
#     changeType(image)
