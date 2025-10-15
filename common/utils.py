import requests
from common.logger import get_logger

logger = get_logger()

def make_request(method, url, data=None, headers=None):
    """Make an API request and return the response."""
    try:
        response = requests.request(method=method, url=url, json=data, headers=headers)
        logger.info(f"{method} {url} -> {response.status_code}")
        return response
    except Exception as e:
        logger.error(f"Request failed: {str(e)}")
        raise
