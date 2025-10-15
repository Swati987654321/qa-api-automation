from common.utils import make_request
from common.config import load_config

config = load_config()
BASE_URL = config["base_url"]

class UsersAPI:
    """Class for handling User-related API operations."""

    @staticmethod
    def get_users(page=2):
        """Fetch list of users."""
        url = f"{BASE_URL}/users?page={page}"
        return make_request("GET", url)

    @staticmethod
    def create_user(name, job):
        """Create a new user."""
        url = f"{BASE_URL}/users"
        data = {"name": name, "job": job}
        return make_request("POST", url, data=data)

    @staticmethod
    def update_user(user_id, name, job):
        """Update existing user."""
        url = f"{BASE_URL}/users/{user_id}"
        data = {"name": name, "job": job}
        return make_request("PUT", url, data=data)

    @staticmethod
    def delete_user(user_id):
        """Delete a user."""
        url = f"{BASE_URL}/users/{user_id}"
        return make_request("DELETE", url)
