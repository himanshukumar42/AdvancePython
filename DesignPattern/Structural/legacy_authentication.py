import requests
from requests.auth import HTTPBasicAuth
from abc import ABC, abstractmethod


class AuthService(ABC):
    @abstractmethod
    def authenticate(self, username: str, password: str):
        pass


class BasicAuthService(AuthService):
    def authenticate(self, username: str, password: str):
        url = "https://example.com/api/login"
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            print("Authenticated successfully via basic Auth.")
            return response.text
        else:
            print("Failed to authenticate via basic auth.")
            return response.text


class OAuth2Service:
    def get_oauth2_token(self, client_id: str, client_secret: str, username: str, password: str, token_url: str):
        data = {
            'grant_type': 'password',
            'client_id': client_id,
            'client_secret': client_secret,
            'username': username,
            'password': password
        }
        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            import pdb; pdb.set_trace()
            token_info = response.json()
            return token_info['access_token']
        else:
            raise Exception(f"failed to retrieve OAUTH2 token: {response.text}")

    def authenticate_with_token(self, token: str, protected_resource_url: str):
        headers = {'Authorization': f"Bearer {token}"}
        response = requests.get(protected_resource_url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return response.text


class OAuth2Adapter(AuthService):
    def __init__(self, oauth2_service: OAuth2Service, client_id: str, client_secret: str, token_url: str):
        self.oauth2_service = oauth2_service
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url

    def authenticate(self, username: str, password: str):
        token = self.oauth2_service.get_oauth2_token(
            client_id=self.client_id,
            client_secret=self.client_secret,
            username=username,
            password=password,
            token_url=self.token_url
        )
        protected_resource_url = "https://authorization-server.com/authorize"
        return self.oauth2_service.authenticate_with_token(token, protected_resource_url)


def main() -> None:
    basic_auth_service = BasicAuthService()
    basic_response = basic_auth_service.authenticate("basic_user", "basic_password")

    oauth2_service = OAuth2Service()
    oauth2_adapter = OAuth2Adapter(
        oauth2_service=oauth2_service,
        client_id="your-client-id",
        client_secret="your-client-server",
        token_url="https://authorization-server.com/authorize"
    )
    oauth2_response = oauth2_adapter.authenticate("funny-gemsbok@example.com", "Stupid-Centipede-71")
    print(f"OAuth2 Auth response: {oauth2_response}")


if __name__ == '__main__':
    main()
