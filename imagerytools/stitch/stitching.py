import cv2
import numpy as np
#Read the images from your directory
dim=(1024,768) 
images=[]
path = 'C:/Users/joaod/Desktop/Rockets/Panorama(teclado).jpg'

for i in range(1,14,1):
    archive = 'foto{}.jpeg'.format(i) 
    photo=cv2.imread(archive,cv2.IMREAD_COLOR)
    photo=cv2.resize(photo,dim,interpolation = cv2.INTER_AREA)   #ReSize to (1024,768)
    high, width = photo.shape[:2] #a montagem é unidirecional, usar essas linhas caso precise girar
    centre = (width/2, high/2)
    rotation = cv2.getRotationMatrix2D(centre, 0, 1.0)
    photo = cv2.warpAffine(photo, rotation, (width, high))
    images.append(photo)

stitcher = cv2.createStitcher()
#stitcher = cv2.Stitcher.create()
ret,panorama = stitcher.stitch(images)

if ret==cv2.STITCHER_OK:
    cv2.imshow('Panorama',panorama)
    cv2.imwrite(path, panorama)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Error during Stitching")
