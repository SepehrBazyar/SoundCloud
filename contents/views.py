from uuid import UUID
from datetime import date
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Album, Track
from .serializers import (
    AlbumBriefSerializer,
    AlbumDetailSerializer,
    TrackDetailSerializer,
)


class AlbumListAPIView(APIView):
    serializer_class = AlbumBriefSerializer

    def get(self, request: Request):
        albums = Album.objects.filter(**request.query_params.dict()).all()
        serializer = self.serializer_class(instance=albums, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save(
            artist=request.user,
            release_date=date.today(),
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
        )


class AlbumDetailAPIView(APIView):
    serializer_class = AlbumDetailSerializer

    def setup(self, request: Request, id: UUID):
        try:
            self.album: Album = Album.objects.get(id=id)
        except Album.DoesNotExist:
            return Response(
                data={"detail": "Album not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return super().setup(request, id)

    def get(self, request: Request, id: UUID):
        serializer = self.serializer_class(
            instance=self.album,
            context={
                "request": request,
            },
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request: Request, id: UUID):
        serializer = self.serializer_class(
            instance=self.album,
            data=request.data,
        )
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def patch(self, request: Request, id: UUID):
        serializer = self.serializer_class(
            instance=self.album,
            data=request.data,
            partial=True,
        )
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def delete(self, request: Request, id: UUID):
        self.album.delete()
        return Response(
            data={"message": "Album Deleted"},
            status=status.HTTP_200_OK,
        )


class TrackDetailAPIView(APIView):
    serializer_class = TrackDetailSerializer

    def setup(self, request: Request, id: UUID):
        try:
            self.track: Track = (
                Track.objects.select_related("album")
                .select_related("album__artist")
                .get(id=id)
            )
        except Track.DoesNotExist:
            return Response(
                data={"detail": "Track not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return super().setup(request, id)

    def get(self, request: Request, id: UUID):
        serializer = self.serializer_class(instance=self.track)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
