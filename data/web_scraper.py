from bs4 import BeautifulSoup
from config.settings import BASE_URL, HEADERS
from core.utils import get_html_content, post_data
from domain.models import WebScraperResult
from core.exceptions import DataNotFoundException

class WebScraper:
    def __init__(self):
        self.base_url = BASE_URL

    def fetch_page_data(self, endpoint: str) -> WebScraperResult:
        url = f"{self.base_url}/{endpoint}"
        html_content = get_html_content(url, HEADERS)
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Add your scraping logic here
        data = {}  # Extracted data

        if not data:
            raise DataNotFoundException("No data found on the page.")
        
        return WebScraperResult(data=data)

    def submit_form(self, endpoint: str, form_data: dict) -> dict:
        url = f"{self.base_url}/{endpoint}"
        response_data = post_data(url, HEADERS, form_data)
        return response_data
