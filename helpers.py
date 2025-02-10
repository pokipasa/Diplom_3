import requests
import random
import string
from data import Urls
from locators.feed_page_locators import FeedPageLocators as Fpl
from locators.main_page_locators import MainPageLocators as Mpl


class CreateOrder:
    @staticmethod
    def authenticated_order_creation_with_ingredients(create_user):
        header = {
                'Authorization': create_user[3]
            }

        body = {
                "email": create_user[0],
                "password": create_user[1],
                "name": create_user[2]
            }
        requests.post(Urls.authorization_url, json=body, headers=header)
        response_ingredients = requests.get(Urls.create_order_url)
        ingredients = response_ingredients.json()["data"]
        body_order = {
                "ingredients": [ingredients[0]["_id"], ingredients[1]["_id"]]
            }

        response = requests.post(Urls.get_orders_url, json=body_order, headers=header)
        return response


class CreateNewUser:
    @staticmethod
    def create_new_user():
        new_body = []
        letters = string.ascii_lowercase
        email = ''.join(random.choice(letters) for _ in range(10)) + '@yandex.ru'
        password = ''.join(random.choice(letters) for i in range(8))
        name = ''.join(random.choice(letters) for i in range(6))

        body = {
                "email": email,
                "password": password,
                "name": name
            }

        response = requests.post(Urls.register_url, json=body)
        a_token = response.json()["accessToken"]
        if response.status_code == 200:
            new_body.append(email)
            new_body.append(password)
            new_body.append(name)
            new_body.append(a_token)

        return new_body
