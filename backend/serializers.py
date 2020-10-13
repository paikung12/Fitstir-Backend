from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tag, Video, VideoPlayList, TagDetail, UserDetail


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagDetail
        fields = ['id', 'name', 'detail']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['id', 'birthday', 'address', 'high', 'weight', 'bmi']


class UserSerializer(serializers.ModelSerializer):
    userdetail_set = UserDetailSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'groups', 'userdetail_set']


class VideoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Video
        fields = ['id', 'image', 'name', 'video', 'tag_type']


class TagSerializer(serializers.ModelSerializer):
    tagdetail_set = TagDetailSerializer(many=True, required=False)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'tagdetail_set']


class VideoPlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPlayList
        fields = ['id', 'image', 'name', 'video']
