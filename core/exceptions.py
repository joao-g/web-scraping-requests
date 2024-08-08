class WebScraperException(Exception):
    """Base class for other exceptions"""
    pass

class NetworkException(WebScraperException):
    """Raised when there is a network related error"""
    pass

class DataNotFoundException(WebScraperException):
    """Raised when the required data is not found"""
    pass

