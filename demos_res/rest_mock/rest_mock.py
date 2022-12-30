"""Mocks a REST API."""
import time


def get_users():
    """Returns a JSON-like dictionary with a list of users. It has a two
    seconds delay to mock the network delay."""
    time.sleep(2)

    return {
        "users": [
            {"firstName": "John", "lastName": "Doe"},
            {"firstName": "Jane", "lastName": "Smith"},
            {"firstName": "Peter", "lastName": "Jones"},
        ]
    }
