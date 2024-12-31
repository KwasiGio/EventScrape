import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_api_key():
    
    API_KEY = os.getenv("EVENTBRITE_API_KEY")

    url = "https://www.eventbriteapi.com/v3/users/me/"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("API Key is working! Here is some basic information:")
        print(response.json())

    else:
        print(f"API Key test has failed. Status code: {response.status_code}")
        print(response.text)


test_api_key()
