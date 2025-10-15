import pytest
from api.users import UsersAPI

class TestUsersAPI:

    def test_get_users(self):
        """Verify fetching users is successful."""
        response = UsersAPI.get_users()
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert len(data["data"]) > 0

    def test_create_user(self):
        """Verify a new user can be created."""
        response = UsersAPI.create_user("Swati", "QA Engineer")
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Swati"
        assert data["job"] == "QA Engineer"

    def test_update_user(self):
        """Verify user update works."""
        response = UsersAPI.update_user(2, "Swati", "Lead QA Engineer")
        assert response.status_code == 200
        data = response.json()
        assert data["job"] == "Lead QA Engineer"

    def test_delete_user(self):
        """Verify user deletion works."""
        response = UsersAPI.delete_user(2)
        assert response.status_code == 204
