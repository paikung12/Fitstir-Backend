from django.urls import path, include
from rest_framework import routers
from backend import views

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register('video', views.VideoViewset)
router.register('tag', views.TagViewset)
router.register('videoplaylist', views.VideoPlayListViewset)
router.register('tagdetail', views.TagDetailViewset)
router.register('user', views.UserViewset)
router.register('userdetail', views.UserDeatailViewset)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
