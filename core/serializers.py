from rest_framework import serializers

from core.models import ActivityPeriod, User


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%b %d %Y %I:%M %p')
    end_time = serializers.DateTimeField(format='%b %d %Y %I:%M %p')

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class UserActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='uid')
    activity_periods = ActivityPeriodSerializer(many=True,
                                                read_only=True,
                                                source='activityperiod_set')

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')
