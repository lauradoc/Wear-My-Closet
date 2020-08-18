
from flask import (Flask, render_template, request, flash, session, redirect, url_for)
import requests
import os
import crud

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

def upload_closet_image(item):
    """upload new file to cloudinary and return url"""
    print(item)
    if item:
        response = cloudinary.uploader.upload(item) 
        image_url = response['secure_url']

    return image_url


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    