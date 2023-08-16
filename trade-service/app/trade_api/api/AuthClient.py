import requests

# API interface for Auth service
class AuthClient:
    @staticmethod
    def get_user(token):
        # pass the token from user
        headers = {"Authorization": token}
        response = requests.request(
            method="GET", url="http://localhost:5003/api/user", headers=headers
        )
        if response.status_code == 200:
            user = response.json()
            return user
