from rest_framework import serializers
from .models import TagType, Tag, Video 


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'video', 'tag']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['type', 'name']


class TagTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagType
        fields = ['name']
