import yaml
import os

def load_config(env="env_test.yaml"):
    """Load configuration from YAML file."""
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_path, "config", env)
    with open(config_path, "r") as file:
        return yaml.safe_load(file)
