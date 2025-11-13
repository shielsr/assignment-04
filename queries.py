from sqlalchemy import text

from models import db

def get_total_orders():
    # Get the total number of orders
    total_query = db.session.execute(text('SELECT COUNT(*) AS total_orders FROM "order";'))
    total_orders = total_query.scalar()
    return total_orders
    
def get_ave_pumpkin_amount():
    # Get the average number of pumpkins per order
    ave_pumpkins_query = db.session.execute(text('''
        SELECT AVG(pumpkin_count) AS avg_pumpkins_per_order
        FROM (
            SELECT order_id, SUM(amount) AS pumpkin_count
            FROM pumpkin_design
            GROUP BY order_id
        ) AS per_order;
    '''))
    ave_pumpkin_amount = ave_pumpkins_query.scalar()
    return ave_pumpkin_amount
    
def get_ave_orders_per_user():
# Get the average number of orders per user
    ave_orders_user_query = db.session.execute(text('''
        SELECT AVG(order_count) AS avg_orders_per_user
        FROM (
            SELECT customer_id, COUNT(*) AS order_count
            FROM "order"
            GROUP BY customer_id
        ) AS per_user;
    '''))
    ave_orders_per_user = ave_orders_user_query.scalar()
    return ave_orders_per_user