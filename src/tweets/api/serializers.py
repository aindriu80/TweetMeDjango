from rest_framework import serializers


from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet # Or from ..models import Tweet

class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True) # also write only
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
        ]