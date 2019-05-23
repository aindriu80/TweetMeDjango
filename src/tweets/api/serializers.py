from django.utils.timesince import timesince
from rest_framework import serializers


from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet # Or from ..models import Tweet

class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True) # also write only
    date_display = serializers.SerializerMethodField()
    timesince= serializers.SerializerMethodField()
    is_retweet = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'is_retweet',
        ]

    def get_is_retweet(self, obj):
        if obj.parent:
            return True
        return False


    def get_date_display(self, obj):
        return obj.timestamp.strftime("%d %b, %Y at %I:%M %p") # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    
    def get_timesince(self, obj):
        return timesince(obj.timestamp)+ " ago"