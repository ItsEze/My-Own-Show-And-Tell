from django.shortcuts import render
from rest_framework.views import APIView, Response
from dotenv import load_dotenv
import requests
import os

# Create your views here.
load_dotenv()

class FortniteStore(APIView):

    def get(self, request):

        apikey = (os.environ['API_KEY'])
        endpoint = f'https://api.fortnitetracker.com/v1/store/'

        headers = {
            "TRN-Api-Key": apikey
        }

        response = requests.get(endpoint, headers=headers)
        responseJSON = response.json()

        # return Response(responseJSON)
        return Response(responseJSON)


