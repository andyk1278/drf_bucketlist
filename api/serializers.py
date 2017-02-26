# api/serizliers.py

from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map Model instance into JSON format"""

    class Meta:
        """Meta class to map serizlier's fields with model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')