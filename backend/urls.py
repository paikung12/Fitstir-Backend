from django.urls import path, include
from django.conf.urls import include, url
from rest_framework import routers
from backend import views

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()

router.register('videos',  views.VideoViewset)
router.register('tag', views.TagViewset)
router.register('tagdetail', views.TagDetailViewset)
router.register('playlist', views.PlaylistVideoViewset)
# router.register('challenge', views.ChallengeViewset)
# router.register('comment', views.CommentViewset)
router.register('user', views.UserViewser)

# router.register('userdetail', views.UserDetailViewset)
# router.register('history', views.ViewHistoryViewset)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('video', views.VideoAPIView.as_view()),
    path('video/<int:pk>', views.VideoAPIViewUpdate.as_view()),


    # path('videos', views.VideoAPIListView.as_view()),

]
