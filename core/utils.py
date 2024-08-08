import requests
from requests import Session
from bs4 import BeautifulSoup

def get_html_content(url: str, headers: dict) -> str:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def post_data(url: str, headers: dict, data: dict) -> dict:
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()

def create_session() -> Session:
    session = Session()
    return session
