import requests
from config.settings import API_URL, HEADERS
from core.utils import create_session
from core.exceptions import NetworkException

class APIService:
    def __init__(self):
        self.session = create_session()
        self.api_url = API_URL

    def get_info_by_cep(self, cep: str) -> dict:
        url = f"{self.api_url}/cep/{cep}"
        try:
            response = self.session.get(url, headers=HEADERS)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise NetworkException(f"Error fetching data for CEP {cep}: {str(e)}")
