import requests


class AuthClient:
    @staticmethod
    def get_user(token):
        headers = {"Authorization": token}
        response = requests.request(
            method="GET", url="http://cuser-service:5003/api/user", headers=headers
        )
        if response.status_code == 401:
            return False
        user = response.json()
        return user
