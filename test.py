from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import subprocess
import os

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'images/'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/<var>', methods=['GET'])
def get_var(var):
    print(var)
    return jsonify(var)

@app.route('/name', methods=['POST'])
def call_name():
    if 'file' not in request.files:
        return jsonify(error='No file part'), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify(error='No selected file'), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'pic.jpg'))
        from main import preprocess
        output = preprocess()

        return jsonify(output)


       

    return jsonify(error='Invalid file type'), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3200, debug=True)
