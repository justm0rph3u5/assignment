from flask import Flask, render_template, request, send_file, jsonify

from werkzeug.utils import secure_filename
import os.path
from flask_autoindex import AutoIndex


#DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
UPLOAD_DIRECTORY = "/Users/dshukla/Desktop/assignment/filesystem"




ppath = "/Users/dshukla/Desktop/assignment/"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
AutoIndex(app, browse_root=ppath)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload')
def upload_file():
   return render_template('index.html')


@app.route('/uploader', methods=['POST'])
def uploader_file():
    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonify('No file part')

        if file.filename == '':

            return jsonify('No selected file')
        if file and allowed_file(file.filename):

            file.save(secure_filename(file.filename))

            return jsonify('file uploaded successfully')
        else:
            return jsonify('invalid file extension')
    else:
        return jsonify('Unsupported Request Method')

'''   Old method
         def uploader_file():
                if request.method == 'POST':
                    f = request.files['file']
                    f.save(secure_filename(f.filename))
                    return file uploaded successfully'''


@app.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return render_template('list.html', contents=files)
    return jsonify(files)

@app.route("/download", methods=['GET'])
def download():
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return render_template('download.html', contents=files)

@app.route('/downloader/<filename>', methods=['GET'])
def download_file(filename):
    path = os.path.join(UPLOAD_DIRECTORY, filename)
    print(path)
    return send_file(path, as_attachment=True)

@app.route("/delete", methods=['GET'])
def deleter():
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return render_template('delete.html', contents=files)

@app.route('/deleter/<filename>', methods=['GET'])
def deleter_file(filename):
    path = os.path.join(UPLOAD_DIRECTORY, filename)
    os.remove(path)
    return jsonify({"response":"delete successful"})

if __name__ == '__main__':
    app.run(port=5000,debug=True)
