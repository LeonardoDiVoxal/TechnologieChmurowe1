# importing Flask and other modules
from flask import Flask, request, render_template
import cv2
import requests
from flask_restful import Resource, Api

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       url = request.form.get("url")
       data = requests.get(url).content
       with open("image.jpg", "wb") as f:
            f.write(data)
            f.close()
            print('url', url)
            image = cv2.imread('image.jpg')
            image = cv2.resize(image, (700, 400))

            hog = cv2.HOGDescriptor()
            hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
            # detect people in the image
            (rects, weights) = hog.detectMultiScale(image, winStride=(2, 2), padding=(16, 16), scale=1.05)

       return {'peopleCount': len(rects)}
    return render_template("form.html")

if __name__=='__main__':
   app.run()
