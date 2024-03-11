from rest_framework import serializers
from core.abstract.serializers import AbstractSerializer
from core.user.models import User
from django.conf import settings 

class UserSerializer(AbstractSerializer):
    posts_count = serializers.SerializerMethodField()

    def get_posts_count(self, instance):
        return instance.post_set.all().count()

    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = ['id', 'username', 'name', 'first_name', 'last_name', 'bio', 'avatar', 'email', 'is_active', 'created', 'updated', 'posts_count']
        # List of all the fields that can only be read by the user
        read_only_fields = ['is_active']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['avatar']:
            return representation
        if settings.DEBUG:
            request = self.context.get('request')
            representation['avatar'] = request.build_absolute_uri(representation['avatar'])
            return representation