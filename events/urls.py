'''
Created on 20 Dec 2020

@author: ozans
'''
from django.urls import include, path
from rest_framework import routers
from . import rest_views

from . import views

router = routers.DefaultRouter()
router.register(r'events', rest_views.EventViewSet)
router.register(r'sessions', rest_views.SessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    #path('', views.index, name='index'),    
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='read_event'),
    path('events/<int:pk>/update', views.EventUpdateView.as_view(), name='update_event'),
    path('events/create', views.EventCreateView.as_view(), name='create_event'),
    path('events/list', views.EventListView.as_view(), name='list_events'),
    path('events/<int:pk>/delete', views.EventDeleteView.as_view(), name='delete_event'),
    
    path('sessions/<int:pk>/', views.SessionDetailView.as_view(), name='read_session'),
    path('sessions/<int:pk>/update', views.SessionUpdateView.as_view(), name='update_session'),
    path('sessions/create', views.SessionCreateView.as_view(), name='create_session'),
    path('sessions/list', views.SessionListView.as_view(), name='list_sessions'),
    path('sessions/<int:pk>/delete', views.SessionDeleteView.as_view(), name='delete_session'),
    

]