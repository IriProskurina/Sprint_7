import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generators import generate_courier_body
from methods.courier_methods import CourierMethods


@pytest.fixture
def generate_courier_data():
    courier_body = generate_courier_body()
    login = courier_body['login']
    password = courier_body['password']
    yield [courier_body, login, password]
    courier_id = CourierMethods.get_courier_id( login, password)
    CourierMethods.delete_courier(courier_id)

