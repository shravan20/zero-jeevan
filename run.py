from app import create_app
import app.config as config
import os
from dotenv import load_dotenv

load_dotenv()

app = create_app()

if __name__ == '__main__':
    port = os.getenv('PORT', config.Config.PORT)
    app.run(debug=True, port=int(port))

