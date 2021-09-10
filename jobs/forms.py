from django import forms
import django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Job


class JobCreateForm(UserCreationForm):
    class Meta:
        model = Job

def add_job(request):
    if request.method == 'POST':
        form = JobCreateForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save()
            return render('job-home')
    else:
        form = JobCreateForm()
    