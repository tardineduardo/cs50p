from PIL import Image
from PIL import ImageOps
import os.path
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

fileType1 = os.path.splitext(sys.argv[1])[1]
fileType2 = os.path.splitext(sys.argv[2])[1]

if fileType1 != fileType2:
    sys.exit("Input and output have different extensions")
if fileType1 not in ['.jpg', '.jpeg', '.png']:
    sys.exit("Invalid input")
if fileType2 not in ['.jpg', '.jpeg', '.png']:
    sys.exit("Invalid input")

before = Image.open(sys.argv[1])
shirt = Image.open('shirt.png')
shirt_size = shirt.size
before_resized = ImageOps.fit(before, shirt_size)
before_resized.paste(shirt, mask=shirt)
before_resized.save(sys.argv[2])
