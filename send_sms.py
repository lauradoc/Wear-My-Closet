# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

from flask import (Flask, render_template, request, flash, session, redirect, url_for)
import requests
import os
import crud

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]
client = Client(account_sid, auth_token)


def send_message_to_user(new_checkout_item):

    message = client.messages \
                    .create(
                        body=f'Your item - {new_checkout_item.item.item_name} - has been checked out by {new_checkout_item.checkout.user.first_name} {new_checkout_item.checkout.user.last_name}. Send them a message @ {new_checkout_item.item.user.phone} to arrange exchange!',
                        from_='+14158776117',
                        to=f'+1{new_checkout_item.item.user.phone}'
                    )

    return message.sid




