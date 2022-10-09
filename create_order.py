# This script produces a large volume of random data.
import datetime
import random

order = {"id": 0, "timestamp": "", "lastname": "", "firstname": "", "address": "", "city": "",
         "state": "", "zip": "", "items": []}
item = {"sku": "", "description": "", "price": "", "quantity": ""}


def generate_random_sku():
    return "SKU" + str(random.randint(0, 1000000))


def generate_random_item():
    item["sku"] = generate_random_sku()
    item["description"] = "Description for " + item["sku"]
    item["price"] = random.random() * 100
    item["quantity"] = random.randint(0, 100)
    return item


def generate_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


order_id = 0


def generate_random_order():
    order["id"] = f"{++order_id}"
    order["timestamp"] = generate_timestamp()
    order["lastname"] = "Lastname" + str(random.randint(0, 1000000))
    order["firstname"] = "Firstname" + str(random.randint(0, 1000000))
    order["address"] = "Address" + str(random.randint(0, 1000000))
    order["city"] = "City" + str(random.randint(0, 1000000))
    order["state"] = "State" + str(random.randint(0, 1000000))
    order["zip"] = "Zip" + str(random.randint(0, 1000000))
    order["items"] = []
    for i in range(0, random.randint(1, 10)):
        order["items"].append(generate_random_item())
    return order