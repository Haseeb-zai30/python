import cv2 as cv
def dimensions(image, scale=0.5):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    return (width, height)


img = cv.imread("pics/img(7).jpg")
cv.imshow("image", img)
img=cv.resize(img,dimensions(img))#image resizing
img=gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("image", img)
blur = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("blur", blur)
edges = cv.Canny(img, 125, 175)
cv.imshow("edges", edges)
cv.waitKey(0)

