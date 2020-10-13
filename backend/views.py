from django.http import HttpResponse
from django.shortcuts import render
from .serializers import VideoSerializer, TagSerializer, VideoPlayListSerializer, TagDetailSerializer, UserDetailSerializer, UserSerializer
from .models import Video, Tag, VideoPlayList, TagDetail, UserDetail
from rest_framework import viewsets
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.

def index(request):
    return HttpResponse('hello world')


class VideoViewset(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tag_type']


class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class VideoPlayListViewset(viewsets.ModelViewSet):
    queryset = VideoPlayList.objects.all()
    serializer_class = VideoPlayListSerializer

class TagDetailViewset(viewsets.ModelViewSet):
    queryset = TagDetail.objects.all()
    serializer_class = TagDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['detail']

class UserDeatailViewset(viewsets.ModelViewSet):
    queryset =  UserDetail.objects.all()
    serializer_class = UserDetailSerializer



class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]



