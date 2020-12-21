'''
Created on 21 Dec 2020

@author: ozans
'''
from events.models import Event, Session
from django import forms


class EventCreateForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())
    
    
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date', 'timezone']
        
class SessionCreateForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())
    
    
    class Meta:
        model = Session
        fields = ['name', 'start_date', 'end_date', 'speaker', 'event']
        
        

#class ActionChooseForm(forms.Form):
#    name = forms.CharField()
#    message = forms.CharField(widget=forms.Textarea)

