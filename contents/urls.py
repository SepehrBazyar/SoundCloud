from django.urls import path
from .views import (
    AlbumListAPIView,
    AlbumDetailAPIView,
)


app_name = "contents"
urlpatterns = [
    path("albums/", AlbumListAPIView.as_view(), name="list"),
    path("albums/<uuid:id>/", AlbumDetailAPIView.as_view(), name="detail"),
]
