from datetime import date, datetime
from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Company, Job, Skill, Language, Country, City
from urllib.parse import urlparse
from django.contrib.auth.models import User
# from . import helperFunctions
import io
from jobs import helperFunctions
import threading

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

def jobUpdate(request):
    t1 = threading.Thread(target=accentureJobUpdate, daemon=True)
    t1.start()
    # t1 = threading.Thread(target=bcgJobUpdate)
    # t1.setDaemon(True)
    # t1.start()
    return render(request, 'jobs/empty.html', {})

def accentureJobUpdate():
    comp = Company.objects.all().filter( name = "Accenture" ).first()
    newJobs = helperFunctions.getAccentureJobs()
    updateJobModel( newJobs, comp )






## Helper Function
def updateJobModel(newJobs, comp):
    for job in Job.objects.all():
        if job.url in newJobs:
            if 'active' in newJobs[job.url]:
                job = newJobs[job.url]['active']
                job.save()
            newJobs.pop(job)
        else:
            job.active = False
    for link in newJobs:
        job = Job( title = newJobs[link]['title'], url = link, company = comp )
        if 'skill' in newJobs[link]:
            for sk in newJobs[link]['skill']:
                job.skills.add( Skill.objects.all().filter( name = sk ).first() )
        if 'description' in newJobs[link]:
            job.description = newJobs[link]['description']
        if 'country' in newJobs[link]:
            job.country = Country.objects.all().filter( name = newJobs[link]['country'] ).first()
        if 'city' in newJobs[link]:
            job.city = City.objects.all().filter( name = newJobs[link]['city'] ).first()
        if 'language' in newJobs[link]:
            job.language = Language.objects.all().filter( name = newJobs[link]['language'] ).first()
        if 'date_posted' in newJobs[link]:
            job.date_posted = datetime.date(newJobs[link]['date_posted']['year'], newJobs[link]['date_posted']['month'], newJobs[link]['date_posted']['day'])
        if 'url' in newJobs[link]:
            job.url = newJobs[link]['url']
        if 'active' in newJobs[link]:
            job.active = newJobs[link]['active']
        job.save()
