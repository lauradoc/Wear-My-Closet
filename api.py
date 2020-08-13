"""Cloudinary API"""

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

import cloudinary 
import cloudinary.uploader
import cloudinary.api


cloudinary.config( 
  cloud_name = os.environ["cloud_name"], 
  api_key = os.environ["cloudinary_api_key"], 
  api_secret = os.environ["cloudinary_api_secret"]
)


def upload_image(file):
    uploaded = cloudinary.uploader.upload(file) 
    image_url = uploaded['secure_url']

    return image_url

