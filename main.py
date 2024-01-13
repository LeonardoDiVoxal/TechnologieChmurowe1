'''
import cv2

img = cv2.imread('airport_terminal1.jpg')
img = cv2.resize(img, (720, 432))

print(type(img))
print(img.shape)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
# import required libraries
import cv2

# Reading the Image
image = cv2.imread('airport_terminal1.jpg')
image = cv2.resize(image, (720, 432))

# initialize the HOG descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# detect humans in input image
(humans, _) = hog.detectMultiScale(image, winStride=(4, 4),
padding=(16, 16), scale=1.1)

# getting no. of human detected
print('Human Detected : ', len(humans))

# loop over all detected humans
for (x, y, w, h) in humans:
   pad_w, pad_h = int(0.15 * w), int(0.01 * h)
   cv2.rectangle(image, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)

# display the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
import cv2

# Reading the Image
image = cv2.imread('queue_line1.jpg')
image = cv2.resize(image, (720, 432))

# initialize the HOG descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# detect humans in input image
(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
padding=(16, 16), scale=1.1)

# loop over all detected humans
for (x, y, w, h) in rects:
   cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# getting no. of human detected
print('Human Detected : ', len(rects))

# display the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
