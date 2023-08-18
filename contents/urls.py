from django.urls import path
from .views import (
    AlbumListAPIView,
    AlbumDetailAPIView,
    TrackDetailAPIView,
)


app_name = "contents"
urlpatterns = [
    path("albums/", AlbumListAPIView.as_view(), name="album-list"),
    path("albums/<uuid:id>/", AlbumDetailAPIView.as_view(), name="album-detail"),
    path("tracks/<uuid:id>/", TrackDetailAPIView.as_view(), name="track-detail"),
]
