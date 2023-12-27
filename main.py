import os
from dotenv import load_dotenv
import client


def main():
    load_dotenv()
    CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")


if __name__ == "__main__":
    main()
