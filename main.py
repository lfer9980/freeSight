import socket
from app import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app()

if __name__ == "__main__": 
    app.run(host =  "192.168.100.8",
            port = 8080)