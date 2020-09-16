![](https://github.com/lauradoc/Wear-My-Closet/blob/master/static/img/wear%20my%20closet.png)
###### Wear My Closet is a web application designed for virtual closet sharing among friends in an effort to reduce material consumption and extend the life span of our clothes. I came up with a virtual way to loan and/or borrow items in your own closet by using python as the main backend language and javascript to amplify the front end experience.


## Contents
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Future State](#future-state)
* [Installation](#installation)

## <a name="tech-stack"></a>Technologies

* Tech Stack: Python, JavaScript (AJAX, JSON), HTML, CSS, SQL, Flask, jQuery, Bootstrap, Jinja, PostgreSQL
* APIs: Cloudinary Upload API, Twilio Messaging API

## <a name="features"></a>Features

### Login Page
Users must login or create an account before viewing any features of Wear My Closet. 
![](https://res.cloudinary.com/lowdock/image/upload/v1600221374/Screen_Shot_2020-09-15_at_7.59.44_PM_noxhqh.png)

### Homepage
After login a user is automatically sent to the homepage where they can join an existing community that they are not currently a member of or create a new community by providing a name and brief description. Otherwise they can continue on to the following features.
![](https://res.cloudinary.com/lowdock/video/upload/v1600221823/Homepage_wj70h0.mp4)

### My Community
A user can be a member of several communities so they first select the one they'd like to view. Upon selection all items from all members of the community will load onto the page. A user will be able to see what items are available to borrow or unavailable according to the item status and the 'Add to Cart' button disabled. If they select an item to add to their cart an alert will confirm. They can continue to browse or move their cart.
![](https://res.cloudinary.com/lowdock/video/upload/v1600221868/My_Community_aimatl.mp4)

### My Closet
This is a user's item inventory. They can check in items that have been returned and can also upload new items to their closet through Cloudinary.
![](https://res.cloudinary.com/lowdock/video/upload/v1600221979/My_Closet_acjohb.mp4)

### My Cart
To complete the checkout process a user selects their return date or removes the item. Once they submit their order the order summary appears and a text notification is sent to the item owner to initiate the exchange.
![](https://res.cloudinary.com/lowdock/video/upload/v1600221924/My_Cart_tu2ldm.mp4)

### My Account
The summary page includes a list of community memberships, checkout items, and items in their inventory.

## <a name="future"></a>Future Additions

* Add google maps feature to track location of items
* Add specific sizing attribute
* Add search filters to My Community page
* Add ability to remove items from My Closet
* Add text notifications as reminders to the user to return borrowed item
* Change alert to flash notification when item is added to cart

## <a name="installation"></a>Installation
Using Wear My Closet on your own:

Required:
- Python3
- PostgreSQL
- [Cloudinary Account](https://cloudinary.com/documentation)
- [Twilio Messaging API](https://www.twilio.com/docs/api)

Clone or fork this repo:
```
$ https://github.com/lauradoc/Wear-My-Closet
```

Create and activate a virtual environment inside Wear My Closet Directory:
```
$ virtualenv env
$ source env/bin/activate
```

Install the requirements:
```
$ pip install -r requirements.txt
```

Create a ```secrets.sh``` file and add your API keys:
```
export cloud_name="YOUR_CLOUD_NAME_HERE"
export cloudinary_api_key="YOUR_KEY_HERE"
export cloudinary_api_secret="YOUR_SECRET_KEY_HERE"

export account_sid="YOUR_KEY_HERE"
export auth_token="YOUR_TOKEN_HERE"
```

Activate secrets file in your virtual environment:
```
$ source.secrets.sh
```

Set up database:
```
$ createdb closets
```

Run the server:
```
$ python3 server.py
```

## About Laura Docherty
Welcome to Laura's first independent project, Wear My Closet. Laura’s career highlights 5 years of sales and marketing experience, particularly well-versed in startup environments. With a self-starter mindset she has been a member of a founding startup fitness studio and most recently moved to CA for a role in sustainable product marketing. When covid affected her career Laura took it as an opportunity to learn something new that would be the risk and push she needed to really believe in her potential.

As a junior software developer she is excited to bring her energy and teamwork to a company that upholds a global, human-centric business model to begin her new career path. Away from the computer she is an active runner and coach elevating her ambitions through investments that make her feel alive.