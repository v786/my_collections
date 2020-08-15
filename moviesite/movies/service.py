import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings

def fetch_movies(request, format=None):
    url = request
    payload = {}
    response = requests.request("GET", url, headers={}, data=payload, auth = HTTPBasicAuth(settings.API_KEY, settings.SECRET))
    json_response = response.json()
    return json_response