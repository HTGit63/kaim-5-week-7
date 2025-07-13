# scrape/utils.py

import os
import logging
from dotenv import load_dotenv

def load_config():
    """
    Load environment variables from .env and return a dict of needed values.
    """
    load_dotenv()  # reads .env in project root by default
    config = {
        'api_id': os.getenv('API_ID'),
        'api_hash': os.getenv('API_HASH'),
        'session_name': os.getenv('SESSION_NAME', 'session'),
        'db_host': os.getenv('DB_HOST'),
        'db_port': os.getenv('DB_PORT'),
        'db_user': os.getenv('DB_USER'),
        'db_password': os.getenv('DB_PASSWORD'),
        'db_name': os.getenv('DB_NAME')
    }
    missing = [k for k,v in config.items() if v is None]
    if missing:
        raise RuntimeError(f"Missing env vars: {missing}")
    return config

def get_logger(name=__name__):
    """
    Simple logger configuration.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = "[%(asctime)s] %(levelname)s %(name)s: %(message)s"
        handler.setFormatter(logging.Formatter(fmt))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
