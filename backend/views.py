from django.http import HttpResponse
from django.shortcuts import render
from .serializers import VideoSerializer, TagSerializer, TagTypeSerializer
from .models import Video, Tag, TagType
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


class TagTypeViewset(viewsets.ModelViewSet):
    queryset = TagType.objects.all()
    serializer_class = TagTypeSerializer
