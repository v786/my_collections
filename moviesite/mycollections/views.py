from rest_framework import status
from django.conf import settings
from users.models import User
from .models import MyCollection
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MyCollectionSerializer
from rest_framework.decorators import api_view


class MyCollectionAPIView(APIView):
    serializer_class = MyCollectionSerializer

    def post(self, request):
        data = request.data
        current_user = request.user
        user = User.objects.filter(email=current_user)
        data['user'] = User.objects.filter(email=current_user).first()
        serializer = self.serializer_class(data=data)
        serializer.create(data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        snippets = MyCollection.objects.all()
        serializer = MyCollectionSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, uuid):
    """
    Retrieve, update or delete a code collection.
    """
    try:
        collection = MyCollection.objects.filter(uuid=uuid).first()
    except collection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MyCollectionSerializer(collection)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MyCollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
