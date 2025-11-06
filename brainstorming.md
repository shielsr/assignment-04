# Project goal

The goal of the project is to sell bespoke carved pumpkins at Halloween, and to allow users to create their own pumpkins.

# What to build

An e-commerce website with the ability for customers to create and order custom pumpkins.

# Personas

Customer
The business owner

# User stories

As a .... I want to ... so that I ....

As a customer, I want to buy a carved pumpkin, so I can put it on display for Halloween.

As a customer, I want to customise the appearance of my pumpkin, so that my pumpkin is unique to me.

As a customer, I want to buy multiple different pumpkins at the same time, so that I can display different ones.

TO DO As a customer, I want to select a date for my pumpkin to be delivered, so I can recevie it in time for Halloween.

As a customer, I want to see a final 'Confirm your order' page, so I can double check that my order is correct.

As a customer, I want to log in to my account, so I can see details of my current & past orders.


As the business owner, I want to take orders from customers, so I can sell my products for Halloween.

TO DO (THE LOGIN PART) As the business owner, I want to log in to my 'admin' account, so I can see what orders customers have placed.

[MAYBE] As the business owner, I want to only allow a certain amount of pumpkin deliveries per day, so I am not overwhelmed with work.


# Nouns/entities

* Customers
* Admins
* Pumpkins
* Orders

# Attributes

* Customer: user id [Primary], first name, surname, email, delivery address, phone, password
* Admin: admin id [Primary], first name, surname, email, phone, password
* Order: order id [Primary], date and time, customer id [Foreign], status 
* Pumpkin design: design id [Primary], order id [Foreign], eyes, mouth, size, amount


# Page/routes to create

* Home
* Create a pumpkin
* Order confirmation
* Log in
* My account
* Orders (Current & History)
* Order page (individual)



