from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2
import pathlib
import peopleCounter

app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads')

app.config['UPLOAD'] = upload_folder


def generate_custom_name(original_file_name):
    return "doObrobki" + pathlib.Path(original_file_name).suffix


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['img']
        filename = generate_custom_name(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)

        # os.system('python peopleCounter.py')

        image = cv2.imread('static/uploads/doObrobki.png')
        # image = cv2.resize(image, (700, 400))

        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        # detect people in the image
        (rects, weights) = hog.detectMultiScale(image, winStride=(2, 2), padding=(16, 16), scale=1.05)

        for (x, y, w, h) in rects:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        ile_osob = len(rects)
        print(ile_osob)
        cv2.imwrite('static/uploads/PeopleDetected.png', image)

        img = os.path.join(app.config['UPLOAD'], 'PeopleDetected.png')
        return render_template('image_render.html', img=img, ile_osob=ile_osob)
    return render_template('image_render.html')


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


if __name__ == '__main__':
    app.run(debug=True, port=8001)
