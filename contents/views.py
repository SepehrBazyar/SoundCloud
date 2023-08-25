from datetime import date
from django.db.models import Sum
from rest_framework import status, generics, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from core.permissions import IsOwnerOrReadOnlyPermission
from core.paginations import CustomPagination
from .models import Album, Track
from .serializers import (
    AlbumBriefSerializer,
    AlbumDetailSerializer,
    TrackDetailSerializer,
)


class AlbumListAPIView(APIView):
    serializer_class = AlbumBriefSerializer
    permission_classes = [IsAdminUser]

    def get(self, request: Request):
        """Get a list of albums"""
        print(request.user)
        albums = (
            Album.objects.filter(**request.query_params.dict())
            .annotate(duration=Sum("tracks__duration"))
            .all()
        )
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


class AlbumDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView,
):
    lookup_field = "id"
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer
    permission_classes = [IsOwnerOrReadOnlyPermission]


class TrackAPIView(viewsets.ModelViewSet):
    lookup_field = "id"
    lookup_url_kwarg = "id"
    pagination_class = CustomPagination
    queryset = Track.objects.select_related("album").all()

    # def get_queryset(self):
    #     return super().get_queryset().filter(**self.request.query_params.dict())

    @action(["POST"], detail=True, url_path="create")
    def delete_all(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        return Response(
            data={"status": "ok"},
        )

    def get_serializer_class(self):
        return TrackDetailSerializer
