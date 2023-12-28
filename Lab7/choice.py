import random


def choice_one(cursor):
    query = "SELECT name FROM products;"
    cursor.execute(query)

    products = cursor.fetchall()
    product_names = [product[0] for product in products]

    chosen_product = random.choice(product_names)
    return chosen_product