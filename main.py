"""Simple Flask Server with a qr generating web form"""
import os.path

from qrcodegenerator import create_qr_code_image
from config import Config

from flask import Flask, send_file, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_get():
    """Default / get function"""
    html = """
	<h1>Make a QR Code</h1>
	<form method="POST" action="/">
		<label for="qr_url">QR URL:</label>
		<input type="text" name="qr_url" id="qr_url" value="http://njit.edu">
		<br>
		<input type="submit" value="Submit">
	</form>
    """
    return html

@app.route("/", methods=["POST"])
def index_post():
    """Default / post function"""
    full_path = os.getcwd()
    qr_url = request.form.get("qr_url")

    directory_path_and_filename = os.path.join(
		full_path,
  		Config.QR_CODE_IMAGE_DIRECTORY,
		Config.QR_CODE_DEFAULT_FILE_NAME
	)

    qr_img = create_qr_code_image(qr_url)
    for _ in range(0,1):
        while True:
            try:
                qr_img.save(directory_path_and_filename)
            except FileNotFoundError:
                qr_image_directory = Config.QR_CODE_IMAGE_DIRECTORY
                new_directory_path = os.path.join(full_path, qr_image_directory)
                os.mkdir(new_directory_path)
                continue
            break
    return send_file(directory_path_and_filename, mimetype="image/png")
