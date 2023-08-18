from rest_framework import serializers
from .models import Album


class AlbumBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ("id", "name", "rating")

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

    class Meta:
        model = Album
        fields = ("name", "rating", "release_date", "tracks")
