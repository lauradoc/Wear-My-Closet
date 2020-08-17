
from flask import (Flask, render_template, request, flash, session, redirect, url_for)
import requests
import os

import cloudinary 
import cloudinary.uploader
import cloudinary.api

app = Flask(__name__)

cloud_name = os.environ["cloud_name"]
cloudinary_api_key = os.environ["cloudinary_api_key"]
cloudinary_api_secret = os.environ["cloudinary_api_secret"]

cloudinary.config( 
  cloud_name = cloud_name, 
  api_key = cloudinary_api_key, 
  api_secret = cloudinary_api_secret  
)

@app.route('/mycloset', methods=['POST'])
def upload_closet_image(file):

    image_name = request.files.get('file')
    # item_name = request.form.get('item_name')
    # if item_name is None:
    #     pass
    # public_id = item_name.replace(' ', '')
    if image_name:
        response = cloudinary.uploader.upload(image_name) 
        image_url = response['secure_url']

    return render_template('mycloset.html', image_url=image_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    