import os
from flask import Flask, flash, request, redirect, url_for, session, render_template
from werkzeug.utils import secure_filename
from object_detection import init_detector, detect_objects

UPLOAD_FOLDER = './static/uploads'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

detector = init_detector()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    print('here upload')
    if request.method == 'POST':

        file = request.files['file']

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            execution_path = os.getcwd();
            uploads_static_path = os.path.join(execution_path, 'static')
            upload_path = os.path.join(uploads_static_path, 'uploads')
            result_static_path = os.path.join(execution_path, 'static')
            result_path = os.path.join(result_static_path, 'result')

            out_name = os.path.join(result_path, filename)
            in_name = os.path.join(upload_path, filename)

            detections = detect_objects(in_name, out_name, detector)


            return {'response': 'OK', 'filename': filename}
    return {response: 'Error'}



if __name__ == "__main__":
    app.run(debug=False)

