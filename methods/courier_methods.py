import data
import requests


class CourierMethods:
    @staticmethod
    def create_courier(body):
        return requests.post(data.Url.COURIER_URL, json=body)

    @staticmethod
    def login_courier(login, password):
        login_password = {'login': login, 'password': password}
        return requests.post(data.Url.LOGIN_URL, json=login_password)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{data.Url.COURIER_URL}/{courier_id}", json={
            "id": courier_id})

    @staticmethod
    def get_courier_id(login, password):
        login_password = {'login': login, 'password': password}
        responce = requests.post(data.Url.LOGIN_URL, json=login_password)

        return responce.json()['id']