import cv2
from flask import Flask
from flask_restful import Resource, Api

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

app = Flask(__name__)
api = Api(app)


class PeopleCounter(Resource):
    def get(self):
        # load image
        image = cv2.imread('airport_terminal1.jpg')
        image = cv2.resize(image, (700, 400))

        # detect people in the image
        (rects, weights) = hog.detectMultiScale(image, winStride=(2, 2), padding=(16, 16), scale=1.05)

        for (x, y, w, h) in rects:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imwrite('static/uploads/PeopleDetected.png', image)
        return {'peopleCount': len(rects)}


api.add_resource(PeopleCounter, '/')

if __name__ == '__main__':
    app.run(debug=True)

'''
# draw the bounding boxes
for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# show the output images
cv2.imshow("People detector", image)
'''
