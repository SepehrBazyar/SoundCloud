from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    AlbumListAPIView,
    AlbumDetailAPIView,
    TrackAPIView,
)


router = SimpleRouter()
router.register("tracks", TrackAPIView, basename="track")


app_name = "contents"
urlpatterns = [
    path("albums/", AlbumListAPIView.as_view(), name="album-list"),
    path("albums/<uuid:id>/", AlbumDetailAPIView.as_view(), name="album-detail"),
    path("", include(router.urls)),
]
