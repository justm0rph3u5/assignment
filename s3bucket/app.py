import os

from flask import Flask, render_template, request, redirect, send_file, url_for, jsonify

from s3_function import list_files, download_file, upload_file, delete_file, allowed_file




app = Flask(__name__)
UPLOAD_FOLDER = "uploadtest"
BUCKET = "userreports21"




@app.route("/")
def index():
    contents = list_files("userreports21")
    return render_template('index.html', contents=contents)

        # check if the post request has the file part

@app.route("/upload", methods=['POST'])
def upload():

    if request.method == "POST":
        f = request.files['file']

        if 'file' not in request.files:
            return jsonify('No file part')

        if f.filename == '':
            return jsonify('No selected file')

        if 'file' and allowed_file(f.filename):

            f.save(f.filename)
            upload_file(f"{f.filename}", BUCKET)

            return jsonify('file uploaded successfully')

        else:
            return jsonify('invalid file extension')
    else:
        return redirect("/")






@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)


@app.route("/delete", methods=['GET'])
def delete():
    contents = list_files("userreports21")
    return render_template('delete.html', contents=contents)

@app.route("/deletefile/<filename>", methods=['GET'])
def deletefile(filename):
    output=delete_file(filename, BUCKET)


    return jsonify({'output':output})


if __name__ == '__main__':
    app.run(debug=True)