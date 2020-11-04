"""creating fake db"""

# from faker import Faker

import os
import json
from random import choice, randint
from datetime import date, timedelta

import crud
import model
import server

# os.system('dropdb closets')
# os.system('createdb closets')

model.connect_to_db(server.app)
model.db.create_all()

# fake = Faker()

# def seed_users():

#     for n in range(10):
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         name = f'{first_name + last_name}'
#         email = f'{name}@test.com'
#         password = 'test'
#         phone = '6517264495'
#         city = 'Saint Paul'

#         new_user = crud.create_user(first_name, last_name, email, password, city, phone)
    
#     crud.create_user('Laura', 'Docherty', 'laurahdocherty@gmail.com', 'test', 'STP', '6517264495')

# seed_users()


def seed_category():

    with open('data/seed_category.json') as f:
        category_data = json.loads(f.read())

    for category in category_data:
        category_name = category['category_name']

        new_category = crud.create_category(category_name)

seed_category()


# def seed_status():

#     with open('data/seed_status.json') as f:
#         status_data = json.loads(f.read())

#     for status in status_data:
#         checkout_status = status['checkout_status']

#         new_status = crud.create_status(checkout_status)

# seed_status()


# def seed_items():

#     with open('data/seed_items.json') as f:
#         items_data = json.loads(f.read())

#     for item in items_data:
#         user_id = item['user_id']
#         item_name = item['item_name']
#         item_description = item["item_description"]
#         image_url = item['image_url']
#         category_name = item['category_name']
#         status_code = item['status']

#         new_item = crud.create_item(user_id, item_name, item_description, image_url, category_name, status_code)

# seed_items()


def seed_community():

    with open('data/seed_community.json') as f:
        community_data = json.loads(f.read())

    for community in community_data:
        community_name = community['community_name']
        community_description = community['community_description']

        new_community = crud.create_community(community_name, community_description)

seed_community()


# def seed_community_member():

#     with open('data/seed_community_member.json') as f:
#         community_member_data = json.loads(f.read())

#     for community_member in community_member_data:
#         community_id = community_member['community_id']
#         user_id = community_member['user_id']

#         new_community_member = crud.create_community_member(community_id, user_id)

# seed_community_member()









