from rest_framework import status
from django.conf import settings
from users.models import User
from .models import MyCollection
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MyCollectionSerializer


class MyCollectionAPIView(APIView):
    serializer_class = MyCollectionSerializer

    def post(self, request):
        data = request.data
        current_user = request.user
        print(current_user)
        user = User.objects.filter(email=current_user)
        print(user)
        data['user'] = User.objects.filter(email=current_user).first()
        serializer = self.serializer_class(data=data)
        print("serializer", data)
        serializer.create(data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        snippets = MyCollection.objects.all()
        serializer = MyCollectionSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

