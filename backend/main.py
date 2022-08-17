from app import app
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

if __name__ == "__main__":
    app.run()