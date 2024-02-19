#!/usr/bin/env python3
from PIL import Image
import os
os.chdir("/home/joey/Pictures/")
for image in os.listdir(os.getcwd()):
	fname = os.path.basename(image)
	f = fname.split(".",1)[0]
	try:
		im = Image.open(image)
		rgb_im = im.convert("RGB")
		rgb_im.rotate(-90).resize((128,128)).save("/home/joey/Pictures/new/"+f+".jpg")
		print("Successfully converted "+image)
	except Exception as ex:
		print("Failed to convert {} because of error: {}".format(image, ex))
os.chdir("/home/joey/Pictures/new/")
for image in os.listdir(os.getcwd()):
	img = Image.open(image)
	print("Format:")
	print(img.format)
	print("Size: ")
	print(img.size)
