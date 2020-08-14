import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import Movie
from .serializers import MovieSerializer
# Create your views here.


@api_view(["GET"])
@permission_classes([AllowAny])
def movies(request, format=None):
    url = "https://demo.credy.in/api/v1/maya/movies/"
    payload = {}
    response = requests.request("GET", url, headers={}, data=payload, auth = HTTPBasicAuth(settings.API_KEY, settings.SECRET))
    json_response = response.json()
    return JsonResponse(json_response)


# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def create(request, format=None):
    url = "https://demo.credy.in/api/v1/maya/movies/"
    payload = {}
    response = requests.request("GET", url, headers={}, data=payload, auth = HTTPBasicAuth(settings.API_KEY, settings.SECRET))
    json_response = response.json()
    page = response.json()
    data = None
    for each in page["results"]:
        data = each
    for key, item in data.items():
        print(key,item)
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(json_response)

@api_view(["GET"])
@permission_classes([AllowAny])
def get(request, format=None):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)