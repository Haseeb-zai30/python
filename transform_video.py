import cv2 as cv
import numpy as np
#capture=cv.VideoCapture("videos/vid(3).mp4")
capture=cv.VideoCapture(0)
while True:
      isTrue, frame = capture.read()
      #cv.imshow("video", frame)
      #translation
      def translate(img,x,y):
          transMat=np.float32([[1,0,x],[0,1,y]])
          dimensions=(img.shape[1],img.shape[0])
          return cv.warpAffine(img,transMat,dimensions)
      translated=translate(frame,100,-100)
      #cv.imshow("translated",translated)

      # rotation
      def rotate(img,angle,rotPoint=None):
          (height,width)=img.shape[:2]
          if rotPoint == None:
              rotPoint=(width//2,height//2)
          rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
          dimensions=(width,height)
          return cv.warpAffine(img,rotMat,dimensions)
      rotated=rotate(frame,45,)
      #cv.imshow("rotated",rotated)
      if cv.waitKey(20) & 0xFF==ord('d'):
          break
