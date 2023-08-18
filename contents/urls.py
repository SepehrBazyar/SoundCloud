from django.urls import path
from .views import (
    AlbumListAPIView,
    AlbumDetailAPIView,
    TrackDetailAPIView,
)


app_name = "contents"
urlpatterns = [
    path("albums/", AlbumListAPIView.as_view(), name="album-list"),
    path("albums/<uuid:pk>/", AlbumDetailAPIView.as_view(), name="album-detail"),
    path("tracks/<uuid:pk>/", TrackDetailAPIView.as_view(), name="track-detail"),
]
