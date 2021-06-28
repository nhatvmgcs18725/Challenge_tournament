from rest_framework import serializers
from testuser.models import NewUsers
from django.conf import settings


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUsers
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
