# Assignment 4 - "Carv"

## Website URL
https://carv-csln.onrender.com/

## Github Repo
https://github.com/shielsr/assignment-04

## Documentation
1. [View setup instructions](setup.md)

2. [View Documentation](documentation.md)

## Project goal
The goal of the project is to allow users to purchase bespoke carved pumpkins for Halloween.

## Features
### As a customer, the user can:
- Log in and out of sessions
- Create new pumpkin designs
- Add their designs to an order
- Submit or cancel the order
- Check their 'my account' page for updates and details on their order

### As a business owner (i.e. an admin), the user can:
- Log in and out of sessions
- See what orders their customers have created
- Change the status of orders

<br>
<br>



# Instructions on how to use the site

<br>

## Navbar

The navbar is responsive on desktop and mobile.

The buttons change based on logged-in status.

The buttons also change based on the user's role (the role is stored in the `user` database table). There are currently only 2 roles, `customer` and `admin`.

<br>

## Signing up

Users can sign up via the form on /signup. They are automatically assigned the role of `customer` in the database.

Their passwords are hashed in the database. 

Once they fill out the form, they are directed to /login, where they can enter their new credentials.

<br>

## Logging in

The site comes seeded with a Customer and an Admin account. [View setup instructions](setup.md)

To access the Admin account, use the username `admin` and password `admin`.

To access the Customer account, use the username `bill` and password `bill`.

<br>

## Homepage welcome card

The card on the homepage changes depending on logged-in status, as well as on whether the user is a Customer or Admin.

<br>

## Creating pumpkins

Only users with the `customer` role can create an order. They'll see the Create button in the navbar.

They fill out the form and submit it. This inserts a new row in the `order`table and a new row in the `pumpkin_design` table.

On the following /order page, the user can add another pumpkin to their order, which takes them to the /add page where they can create another design.

<br>

## Cancelling an order

Cancelling an order deletes that row from the `order` table and 'cascade-deletes' all related rows from the `pumpkin_design` table. 

Customers can cancel an order in two places:

1. On the /order page before they've submitted

2. On the /my-account page, where they can cancel an order as long as it hasn't been marked as 'Delivered' (at which point the Cancel button is not shown)

<br>

##  View my account

Only customers can see links to the /my-account page

Customers can view their previous orders here, along with in-progress ones. As mentioned above, they can cancel orders as long as their status is not `Delivered`.

<br>

## Admin

If a user logs in as an admin (see 'Logging in' above) they can see all orders that can be read from the `order` database table, along with the customer details and pumpkins connected to the order.

Admins can edit the status of orders. This updates the relevant entry in the database.

They can also see statistics.

NOTE: If an admin sets an order to `Delivered`, then the 'Cancel order' button no longer appears for the customer.

