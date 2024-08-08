from data.web_scraper import WebScraper
from services.api_service import APIService

def main():
    scraper = WebScraper()
    api_service = APIService()
    
    # Example usage:
    try:
        # Fetch page data
        result = scraper.fetch_page_data("some-endpoint")
        print(result)
        
        # Use API service to get additional data
        cep_info = api_service.get_info_by_cep("01001000")
        print(cep_info)
        
        # Submit form data
        form_data = {
            # Add your form data here
        }
        response = scraper.submit_form("form-endpoint", form_data)
        print(response)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
