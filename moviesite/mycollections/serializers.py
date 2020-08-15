# import the django rest framework serializers
from rest_framework import serializers
# import our models
from users.models import User
from .models import MyCollection
from moviesite.movies.models import Movie

class MyCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCollection
        fields = ('title', 'description')

    def create(self, validated_data):
        print("validated_data", validated_data)
        items_data = validated_data['movies']
        # if validated_data['user']!= None:
        #     validated_data['user'] = User.objects.filter(pk=validated_data['user']).first()
        my_collection = MyCollection.objects.create(**validated_data)
        my_collection.save()
        for item_data in items_data:
            print(item_data)
            my_collection.movies.add(Movie.objects.filter(uuid = item_data).first())
            print("here")
        return my_collection