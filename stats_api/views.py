from django.shortcuts import render
from rest_framework.views import APIView, Response
from dotenv import load_dotenv
import requests
import os

# Create your views here.
load_dotenv()

class FortniteStats(APIView):

    def get(self, request, platform, user):

        apikey = (os.environ['API_KEY'])
        endpoint = f'https://api.fortnitetracker.com/v1/profile/{platform}/{user}'

        headers = {
            "TRN-Api-Key": apikey
        }

        response = requests.get(endpoint, headers=headers)
        responseJSON = response.json()

        # return Response(responseJSON)
        return Response(responseJSON)