#
#     Andrew Yoder
#	  auy121@psu.edu | andrewyoder1@gmail.com    
#     Mobile Geospatial Systems Group
#     Department of Ecosystem Science and Management
#     The Pennsylvania State University
#     2018/06/14
#

#!/bin/python

import os, PhotoScan

print("---- Script started ----")

# create new photoscan document
doc = PhotoScan.app.document
print("---- Photoscan booted up ----")
# add a new chunk
chunk = doc.addChunk()
print("---- New chunk added ----")

# ask user for folder containing photos
path_photos = PhotoScan.app.getExistingDirectory("Enter folder containing photos:")
path_photos += "/"

image_list = os.listdir(path_photos)
photo_list = list()
for photo in image_list:
	if photo.rsplit(".",1)[1].upper() in ["JPG", "JPEG", "TIF", "PNG"]:
		photo_list.append(path_photos + photo)
		print(photo)
	else:
		print("No photo available")
# lists all photos in folder (optional):
#print(photo_list)

# add photos to chunk
chunk.addPhotos(photo_list)
PhotoScan.app.update
print("---- Added photos ----")

# match photos
chunk.matchPhotos(accuracy=PhotoScan.MediumAccuracy)
print("---- Matched photos ----")
# align photos
chunk.alignCameras()
print("---- Aligned Photos ----")

# build dense cloud
chunk.buildDenseCloud(quality=PhotoScan.MediumQuality)
print("---- Dense cloud built ----")

# build model
chunk.buildModel
print("---- Model built ----")

# build texture
chunk.buildTexture
print("---- Texture built ----")

# save document (WIP)
doc.save()

print("---- Project saved ----")
