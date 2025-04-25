from faker import Faker

fake = Faker()


def generate_courier_body():
    return {
        "login": fake.pystr(min_chars=5,max_chars=5) ,
        "password": (fake.random_int(min=50, max=500)),
        "firstName": fake.first_name()
    }
def generate_order_body(color=None):
    body = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.random_int(min=1, max=20),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=10),
        "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
        "comment": fake.sentence(),
    }
    if color:
        body["color"] = color
    return body