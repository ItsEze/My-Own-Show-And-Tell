import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

apikey = (os.environ['API_KEY'])
endpoint = 'https://api.fortnitetracker.com/v1/stats/kbm/ezekiel_13x'

headers = {
    "TRN-Api-Key": apikey
}

response = requests.get(endpoint, headers=headers)
responseJSON = response.json()

pprint(responseJSON)