import reflex as rx
from decouple import config

DATABASE_URL = config("DATABASE_URL")

config = rx.Config(
    app_name="reflex_app_2nd",
    backend_port=8001,  # Change this to your desired port
    api_url="http://localhost:8001",
    db_url = DATABASE_URL
    
)