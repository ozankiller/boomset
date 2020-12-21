from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Event, Session
from events.forms import EventCreateForm, SessionCreateForm

def index(request):
    return HttpResponse("Hello, world. You're at the events index.")

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'events/eventdetail.html'

class EventListView(generic.ListView):
    model = Event
    paginate_by = 5
    template_name = 'events/eventlist.html'

class EventCreateView(generic.CreateView):
    #model = Event
    #fields = ['name', 'start_date', 'end_date', 'timezone']
    form_class = EventCreateForm
    template_name = 'events/create.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # things
        
        if self.object.start_date > self.object.end_date:
            return HttpResponseRedirect(reverse_lazy('create_event'))
        if (self.object.timezone < -12) or (self.object.timezone > 12):
            return HttpResponseRedirect(reverse_lazy('create_event'))
        
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class EventUpdateView(generic.UpdateView):
    model = Event
    fields = ['name', 'start_date', 'end_date', 'timezone']
    template_name = 'events/update.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # things
        
        if self.object.start_date > self.object.end_date:
            return HttpResponseRedirect(reverse_lazy('update_event'), kwargs={'pk': self.object.pk})
        if (self.object.timezone < -12) or (self.object.timezone > 12):
            return HttpResponseRedirect(reverse_lazy('update_event', kwargs={'pk': self.object.pk}))
        
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class EventDeleteView(generic.DeleteView):
    model = Event
    success_url = reverse_lazy('list_events')
    template_name = 'events/delete.html'



class SessionDetailView(generic.DetailView):
    model = Session
    template_name = 'events/sessiondetail.html'

class SessionListView(generic.ListView):
    model = Session
    paginate_by = 5
    template_name = 'events/sessionlist.html'

class SessionCreateView(generic.CreateView):
    #model = Session
    #fields = ['name', 'start_date', 'end_date', 'speaker','event']
    form_class = SessionCreateForm
    template_name = 'events/create.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # things
        
        if self.object.start_date > self.object.end_date:
            return HttpResponseRedirect(reverse_lazy('create_session'))
        
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class SessionUpdateView(generic.UpdateView):
    model = Session
    fields = ['name', 'start_date', 'end_date', 'speaker','event']
    template_name = 'events/update.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # things
        
        if self.object.start_date > self.object.end_date:
            return HttpResponseRedirect(reverse_lazy('update_session', kwargs={'pk': self.object.pk}))
        
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class SessionDeleteView(generic.DeleteView):
    model = Session
    success_url = reverse_lazy('list_sessions')
    template_name = 'events/delete.html'

