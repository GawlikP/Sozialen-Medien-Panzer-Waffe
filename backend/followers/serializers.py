from rest_framework import serializers 

from .models import UserFollowing

from core.models import Account

class FollowersSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = ['id', 'created', 'profile_id', 'following_profile_id']