import pytest
from common.config import load_config

@pytest.fixture(scope="session")
def base_url():
    """Fixture to load base URL from config."""
    config = load_config()
    return config["base_url"]
