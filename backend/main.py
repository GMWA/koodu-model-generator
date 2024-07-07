from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env
from modelgenerator.server import app

if __name__ == "__main__":
    app.run()