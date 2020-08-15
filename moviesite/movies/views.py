import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
from django.shortcuts import render
from .service import fetch_movies
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
    json_response = fetch_movies(url)
    return JsonResponse(json_response)


# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def create(request, format=None):
    uid = request.data["uuid"]
    url = "https://demo.credy.in/api/v1/maya/movies/"
    page = fetch_movies(url)
    data = None
    for each in page["results"]:
        if(each["uuid"] == uid):
            data = each
            break
    print(data["uuid"])
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        uid = data["uuid"]
        print(uid)
        ob = Movie.objects.filter(uuid = uid)
        if(ob.first() == None):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(page)

@api_view(["GET"])
@permission_classes([AllowAny])
def get(request, format=None):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)