# My design decisions
## User stories

### Roles:
- Customer who wants to buy bespoke carved pumpkins for Halloween
- The business owner who, as an admin, wants to get and process orders

<br>

### Customer user stories:

#### 1. Order the product
[MUST] As a customer, I want to buy a carved pumpkin, so I can put it on display for Halloween.

#### 2. Customise pumpkin appearance
[MUST] As a customer, I want to customise the appearance of my pumpkin, so that my pumpkin is unique to me.

#### 3. Add different products to my order
[MUST] As a customer, I want to buy multiple different pumpkins at the same time, so that I can display different ones.

#### 4. Check before confirming order
[MUST] As a customer, I want to see a final 'Confirm your order' page, so I can double check that my order is correct.

#### 5. Login to my account
[MUST] As a customer, I want to log in to my account, so I can see details of my current & past orders.

#### 6. Cancel an order
[MUST] As a customer, I want to cancel an order, so I can back out of purchasing the product.

<br>

### Business owner user stories:

#### 1. Take orders
[MUST] As the business owner, I want to take orders from customers, so I can sell my products for Halloween.

#### 2. Login as admin
[MUST] As the business owner, I want to log in to my 'admin' account, so I can see what orders customers have placed.

#### 3. Edit order status 
[MUST] As the business owner, I want to change the status of orders, so I can mark them as 'In progress', 'Delivered', etc.

<br>

### Future work:

#### 6. Choose delivery date
[SHOULD] As a customer, I want to select a date for my pumpkin to be delivered, so I can recevie it in time for Halloween.

#### 5. Limit daily deliveries
[SHOULD] As the business owner, I want to only allow a certain amount of pumpkin deliveries per day, so I am not overwhelmed with work.

<br>
<br>


## Content
The site will include:
- Homepage with introduction and different actions depending on user role
- 'Signup' page to allow users to register to Carv
- 'Login' page to allow users to start sessions
Customer-only pages:
- 'Create' page with a form for designing a pumpkin
- 'Order' page with order details and the ability to change, cancel or confirm the order
- 'Add' page allowing users to add another pumpkin to their order
- 'My account' page showing the user's orders, with 'cancel' action on orders that are yet to be delivered 
- 'Thank you' page to show order completion
Admin-only pages:
- 'Admin' page showing all orders in the system

<br>
<br>

## Prioritised tasks:
1. Design database tables in PGadmin
2. Write classes and functions in Python to facilitate the user stories
3. Use Flask to set up templates, routes, etc
4. Use a combination of CSS and Bootstrap for the style and layout of the site
5. Use SQLAlchemy and SQLite for CRUD actions on tables (creating, reading, updating and deleting data)
6. Use Jinja and Javascript for the functionality of the site
7. Set up Postgres on Render.com and deploy app


<br>
<br>

## Wireframes

I created basic wireframes in Figma for mobile and desktop, with the mobile layout responsively catering for tablets too.

<br>
<br>

# My development process
## How I went about it

The following is a step-by-step account of how I did the project, which closely corresponds with the series of commits I made to the repo.

- Brainstormed initial ideas for the assignment
- Wrote user stories and entities
- Fleshed out entities and attributes, and determined what primary and foreign keys I need
- Designed ERD of database tables in PGAdmin and created the tables
- Set up the Flask application and some basic templates, enabling me to create a server and open my templates in Chrome.
- Wrote the HTML of a basic 'Create a pumpkin' form.
- Added CSS and Bootstrap to tidy up the overall site & form appearance
- Created config.py and included secret key code
- Wrote classes in models.py to create tables (initially with SQLite), and mapped out their relationships
- In app.py, set up routes to allow for create, order and thank you pages
- Allowed users to submit a pumpkin design, which inserts a row into the `pumpkin_design` table
- Set up the routes so the `order_id` can be passed through the whole user journey
- Allowed users to add many pumpkin designs to one `order_id` in the order table
- Created /admin page, with a jinja loop listing the orders and a nested loop listing the pumpkins in each order
- Built login/logout authentication
- Improved page template and layout. Included page titles with Jinja.
- Recoded forms for better layout and fixes. Added new Bootstrap styles and custom CSS 
- Added 'Show password' checkbox in forms using Javascript
- Created a /my-account page, showing orders associated with my account
- Added an empty state on the /my-account page where the user hasn't created any orders
- Wrote a `delete_order` function, allowing users to cancel orders on the /order and on the /my-account pages. This cascades down to delete all the connected `pumpkin_designs`
- Wrote update function for the /admin page. Admins can update the status of orders, which the user can see in their account
- Added docstrings for relevant functions
- Spent a lot of time troubleshooting deploying the site to Render.com. Some issues encountered:
    - I had some items missing from my requirements.txt file, e.g. `gunicorn` and `psycopg`
    - Postgres doesn't like `PRAGMA`, which I needed for cascade deleting in Sqlite. Had to remove it.
    - The seed data I triggered with Sqlite didn't work. I had to put them behind a route (/seed)
- Added validation to the /create and /add forms.  Added `required` attribute in the HTML.  In Python, I added `.get()` requests so I could include defaults 
- Fixed error handling on /login page. Now throws an error message using JSON & JS `fetch()` and shown on the page.

<br>
<br>

# Challenges faced

Challenges I faced include:

## 

## Deploying to Render.com
I spent a lot of time troubleshooting deploying the site to Render.com. Some issues encountered:
    - I had some items missing from my requirements.txt file, e.g. `gunicorn` and `psycopg`
    - Postgres doesn't like `PRAGMA`, which I needed for cascade deleting in Sqlite. I had to remove it.
    - The seed data I triggered with Sqlite didn't work. I had to put them behind a route (/seed)

<br>

## User authentication
I didn't use Login Manager in my previous assignments, so it was new to me. I followed Yoni's videos and the following YouTube tutorial to figure out how to apply it. https://www.youtube.com/watch?v=t9zA1gvrTvo&list=PL7yh-TELLS1EyAye_UMnlsTGKxg8uatkM&index=8

<br>

## Hashing passwords
This was another thing that was new to me.

<br> 





## Deploying to Render.com
Now that the app is more complex than in previous assignments, I had to do some troubleshooting to successfully deploy it. This included the following:

## Cascade deleting in SQLite
I wanted, when deleting an order, for the associated pumpkin designs to be deleted from the pumpkin_design table. It took me a while to figure this out, as I didn't realise cascade deletion needed to be 'switched on' in SQLite (i.e. foreign keys needed to be turned on). I added `PRAGMA foreign_keys = ON;` and got it working locally.  But, when switching over to my postgres db on Render.com, the deploy failed. So I had to remove the PRAGMA code. PLEASE NOTE: Cascade deleting now doesn't work locally with SQLite, but it does work on the live site.


## Seeding the tables with data
For future convenience, I wanted to 

<br>
## Bugfixes
I fixed bugs as they came up. I also had a few friends doing user testing, and fixed anything they spotted.