import requests


class AuthClient:
    @staticmethod
    def get_user(token):
        headers = {"Authorization": token}
        response = requests.request(
            method="GET", url="http://localhost:5003/api/user", headers=headers
        )
        if response.status_code == 200:
            user = response.json()
            return user
