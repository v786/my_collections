# import the django rest framework serializers
from rest_framework import serializers
# import our models
from .models import Movie, MyCollection

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MyCollectionSerializer(serializers.ModelSerializer):
    movies = Movie(many=True)

    class Meta:
        model = MyCollection
        fields = ('id', 'title', 'description', 'movies')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        my_collection = MyCollection.objects.create(**validated_data)
        for item_data in items_data:
            item_data['my_collection_id'] = my_collection.id
            Movie.objects.create(**item_data)
        return my_collection