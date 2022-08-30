import os

PROJECT_NAME = os.getenv("PROJECT_NAME", "AWidgets")
DB_NAME = os.getenv("DB_NAME", "awidgets")
DEFAULT_LIST_RESPONSE_LIMIT = int(os.getenv("DEFAULT_LIST_RESPONSE_LIMIT", "100"))
SQLALCHEMY_DATABASE_URI = f"sqlite:///./db/{DB_NAME}.db"
CORS_ORIGINS = "http://localhost"
