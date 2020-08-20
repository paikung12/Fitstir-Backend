from django.urls import path, include
from rest_framework import routers
from backend import views

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register('video', views.VideoViewset)
router.register('tag', views.TagViewset)
router.register('tagType', views.TagTypeViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
