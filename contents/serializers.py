from rest_framework import serializers
from persons.serializers import ArtistSerializer
from .models import Album, Track


class AlbumBriefSerializer(serializers.ModelSerializer):

    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = ("id", "name", "rating", "artist")

    def validate_rating(self, value: int):
        """Validate the rating value for a given value

        :param value: the value to validate the rating
        :raises serializers.ValidationError: if the value is invalid
        :return: the validation result value for the given value
        """
        if not 1 <= value <= 10:
            raise serializers.ValidationError("Invalid Rate Between 1 and 10")

        return value


class AlbumDetailSerializer(serializers.ModelSerializer):

    tracks = serializers.StringRelatedField(read_only=True, many=True)
    releaseDate = serializers.DateField(read_only=True, source="release_date")
    present = serializers.CharField(read_only=True, source="show")

    class Meta:
        model = Album
        fields = ("name", "rating", "releaseDate", "tracks", "present")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["count"] = instance.tracks.count()
        return representation

    # def to_internal_value(self, data):
    #     temp = super().to_internal_value(data)
    #     return temp["data"]


class TrackDetailSerializer(serializers.ModelSerializer):

    album = AlbumBriefSerializer()

    class Meta:
        model = Track
        fields = ("id", "title", "duration", "album")
