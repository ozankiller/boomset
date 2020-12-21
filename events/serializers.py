'''
Created on 21 Dec 2020

@author: ozans
'''
from .models import Event, Session
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id','name', 'start_date', 'end_date', 'timezone', 'url']
        
    def validate(self, attrs):
        if attrs['timezone'] < -12 or attrs['timezone'] > 12:
            raise serializers.ValidationError({"timezone":"Timezone must be between -12 and +12"})
        if attrs['start_date'] > attrs['end_date']:
            raise serializers.ValidationError({"end_date":"End Date must be after Start Date"})
        return serializers.HyperlinkedModelSerializer.validate(self, attrs)


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'name', 'start_date', 'end_date', 'speaker', 'event', 'url']
        
    def validate(self, attrs):
        if attrs['start_date'] > attrs['end_date']:
            raise serializers.ValidationError({"end_date":"End Date must be after Start Date"})
        return serializers.HyperlinkedModelSerializer.validate(self, attrs)