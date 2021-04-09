from django.db.models.base import Model
from rest_framework import fields, serializers

from .models import MovieData


class MovieSerilizer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = MovieData
        fields = ["id", "name", "dutation", "rating", "typ", "image"]
