from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Job
from urllib.parse import urlparse
from django.contrib.auth.models import User
# from . import helperFunctions
import io


# Create your views here.

class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'jobs/home.html'
    ordering = ['title']

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['act'] = not all( not proj.active for proj in Job.objects.all() )
        context['pas'] = not all( proj.active for proj in Job.objects.all() )
        context['mainUser'] = User.objects.filter(id=1).first()
        return context

class JobDetailView(DetailView):
    model = Job
    
    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        context['mainUser'] = User.objects.filter(id=1).first()
        return context

