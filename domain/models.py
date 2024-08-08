class WebScraperResult:
    def __init__(self, data: dict):
        self.data = data

    def __repr__(self):
        return f"<WebScraperResult(data={self.data})>"
