from rest_framework import serializers
from preworktour.models import driverPost
from django.conf import settings


class driverPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = driverPost
        fields = ('id', 'title', 'text', 'image',
                  'price', 'daystart', 'author', 'status')
