import cv2
import requests
from flask import Flask, request
from flask_restful import Resource, Api

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

app = Flask(__name__)
api = Api(app)


class PeopleCounterStatic(Resource):
    def get(self):
        # load image
        image = cv2.imread('airport_terminal1.jpg')
        image = cv2.resize(image, (700, 400))

        # detect people in the image
        (rects, weights) = hog.detectMultiScale(image, winStride=(2, 2), padding=(16, 16), scale=1.05)

        return {'peopleCount': len(rects)}

class PeopleCounterDynamicUrl(Resource):
    def get(self):
        url = request.args.get('url')
        #url = 'https://th.bing.com/th/id/R.5b4a64cde4b76ff0cdfadb4e83f952cc?rik=ErU2l9IJhTJZUQ&riu=http://web.stanford.edu/class/archive/cs/cs106b/cs106b.1206/lectures/stacks-queues/img/queue.png&ehk=OGoFhcXU%2b85adIALQjZDnBnBaStbU8QL1uYCKlDO32o%3d&risl=&pid=ImgRaw&r=0'
        data = requests.get(url).content
        with open("image.jpg", "wb") as f:
            f.write(data)
            f.close()
        print('url', url)

        image = cv2.imread('image.jpg')
        image = cv2.resize(image, (700, 400))

        # detect people in the image
        (rects, weights) = hog.detectMultiScale(image, winStride=(2, 2), padding=(16, 16), scale=1.05)

        return {'peopleCount': len(rects)}

api.add_resource(PeopleCounterStatic, '/')
api.add_resource(PeopleCounterDynamicUrl, '/dynamic')

if __name__ == '__main__':
    app.run(debug=True)

'''
# draw the bounding boxes
for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# show the output images
cv2.imshow("People detector", image)
'''
