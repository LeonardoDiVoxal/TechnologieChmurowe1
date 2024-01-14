from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
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

        img = os.path.join(app.config['UPLOAD'], 'PeopleDetected.png')
        return render_template('image_render.html', img=img)
    return render_template('image_render.html')


if __name__ == '__main__':
    app.run(debug=True, port=8001)
