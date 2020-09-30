from django.http import HttpResponse
from django.shortcuts import render
from .serializers import VideoSerializer, TagSerializer, VideoPlayListSerializer, TagDetailSerializer
from .models import Video, Tag, VideoPlayList, TagDetail
from rest_framework import viewsets


# Create your views here.

def index(request):
    return HttpResponse('hello world')


class VideoViewset(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class VideoPlayListViewset(viewsets.ModelViewSet):
    queryset = VideoPlayList.objects.all()
    serializer_class = VideoPlayListSerializer

class TagDetailViewset(viewsets.ModelViewSet):
    queryset = TagDetail.objects.all()
    serializer_class = TagDetailSerializer
