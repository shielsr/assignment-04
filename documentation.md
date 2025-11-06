# My development process
## How I went about it

The following is a step-by-step account of how I did the project, which closely corresponds with the series of commits I made to the repo.

- Brainstormed initial ideas for the assignment
- Wrote user stories and entities
- Set up the Flask application and some basic templates, enabling me to create a server and open my templates in Chrome.
- Wrote the HTML of a basic 'Create a pumpkin' form.
- Added CSS and Bootstrap to tidy up the overall site & form appearance
- Fleshed out entities and attributes, and determined what primary and foreign keys I need
- Created config.py and included secret key code
- Wrote classes in models.py to create tables (initially with SQLite), and mapped out their relationships
- In app.py, set up routes to allow for create, order and thank you pages
- Allowed users to submit a pumpkin design, which adds a row to the pumpkin_design table
- Allowed users to add many pumpkin designs to one order