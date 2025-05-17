import cv2 as cv
import numpy as np
img = cv.imread("pics/img(6).jpg")
#cv.imshow("image", img)
#translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
 #   cv.imshow("image",transMat)
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
translated=translate(img,100,-100)#-ve x =shift left, -ve y=shift up
cv.imshow("translated",translated)

#rotation
rotated=cv.rotate(img,cv.ROTATE_90_CLOCKWISE)
#rotated=cv.rotate(img,cv.ROTATE_90_COUNTERCLOCKWISE)
#rotated=cv.rotate(img,cv.ROTATE_180)
#cv.imshow("rotated",rotated)
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint == None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img,45,)
cv.imshow("rotated",rotated)
#flip
flip=cv.flip(img,0)
cv.imshow("flip",flip)

#cropping
cropped=img[200:400,300:500]
cv.imshow("cropped",cropped)

cv.waitKey(0)
