import os

import requests
from rest_framework.response import Response
from rest_framework.views import APIView

API_KEY = os.environ.get('MERAKI_REAL_API_KEY')
ORG_NAME = 'TelOne'
NETWORK_NAME = ''

BASE_URL = 'https://api.meraki.com/api/v1'


class MerakiProxyView(APIView):
    def get(self, request, path):
        url = f'{BASE_URL}/{path}'
        headers = {
            'X-Cisco-Meraki-API-Key': API_KEY,
        }
        response = requests.get(url, headers=headers)
        return Response(response.json())

    def post(self, request, path):
        url = f'{BASE_URL}/{path}'
        headers = {
            'X-Cisco-Meraki-API-Key': API_KEY,
            'Content-Type': 'application/json',
        }
        data = request.data
        response = requests.post(url, headers=headers, json=data)
        return Response(response.json())

    def put(self, request, path):
        url = f'{BASE_URL}/{path}'
        headers = {
            'X-Cisco-Meraki-API-Key': API_KEY,
            'Content-Type': 'application/json',
        }
        data = request.data
        response = requests.put(url, headers=headers, json=data)
        return Response(response.json())

    def patch(self, request, path):
        url = f'{BASE_URL}/{path}'
        headers = {
            'X-Cisco-Meraki-API-Key': API_KEY,
            'Content-Type': 'application/json',
        }
        data = request.data
        response = requests.patch(url, headers=headers, json=data)
        return Response(response.json())

    def delete(self, request, path):
        url = f'{BASE_URL}/{path}'
        headers = {
            'X-Cisco-Meraki-API-Key': API_KEY,
        }
        response = requests.delete(url, headers=headers)
        return Response(response.json())
# a98a2806381f3df24318ce9a78a70eafa62d17fe
