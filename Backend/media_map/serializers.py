from django.contrib.gis.geos import Point
from rest_framework import serializers
from .models import Media

class MediaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Media
        fields = '__all__'

    def create(self, validated_data):
        # Check if 'location' key exists in validated_data
        if 'location' in validated_data:
            location_input = validated_data['location']
            # Check if the input is in 'latitude, longitude' format
            if ',' in location_input:
                latitude, longitude = [float(coord.strip()) for coord in location_input.split(',')]
                # Convert to WKT format
                validated_data['location'] = Point(longitude, latitude)

        return super(MediaSerializer, self).create(validated_data)

