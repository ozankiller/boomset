'''
Created on 21 Dec 2020

@author: ozans
'''

from .models import Event, Session
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EventSerializer, SessionSerializer


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class SessionViewSet(viewsets.ModelViewSet):

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]