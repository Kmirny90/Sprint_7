from faker import Faker
import string
import random

fake = Faker()

def generate_couriers_body():
    return {
        "login": fake.user_name()[:10],
        "password": fake.password()[:10],
        "firstName": fake.first_name()[:10]
    }

def generate_order_body(color=None):
    order = {"firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address().replace('\n', ', ')[:50],
        "metroStation": random.randint(1, 50),
        "phone": fake.phone_number()[:15],
        "rentTime": random.randint(1, 7),
        "deliveryDate": fake.date_between(start_date='+1d', end_date='+2w').isoformat(),
        "comment": fake.sentence(nb_words=5)
    }
    if color is not None:
        order["color"] = color
    return order

def generate_string_body(length):

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
