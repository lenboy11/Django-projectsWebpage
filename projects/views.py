from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Project, Link
from urllib.parse import urlparse
from django.contrib.auth.models import User
from . import helperFunctions

# Create your views here.

## Project Views
def home(request):
    context = {
        'projects' : Project.objects.all(),
        'act': not all( not proj.active for proj in Project.objects.all() ),
        'pas': not all( proj.active for proj in Project.objects.all() ),
        'cssFiles': {'projects/css/main.css', 'projects/css/homeCSS.css'},
        'mainUser': User.objects.filter(id=1).first(),
    }
    return render(request, 'projects/home.html', context)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/home.html'
    ordering = ['title']

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['act'] = not all( not proj.active for proj in Project.objects.all() )
        context['pas'] = not all( proj.active for proj in Project.objects.all() )
        context['mainUser'] = User.objects.filter(id=1).first()
        return context

class ProjectDetailView(DetailView):
    model = Project
    
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['Links'] = Link.objects.filter(project = self.get_object())
        context['mainUser'] = User.objects.filter(id=1).first()
        return context

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'content', 'category', 'frontpic', 'url', 'active', 'private']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['mainUser'] = User.objects.filter(id=1).first()
        return context

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'description', 'content', 'category', 'frontpic', 'url', 'active', 'private']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        project = self.get_object()
        return self.request.user == project.author
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['mainUser'] = User.objects.filter(id=1).first()
        return context

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'
    def test_func(self):
        project = self.get_object()
        return self.request.user == project.author
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['mainUser'] = User.objects.filter(id=1).first()
        return context

def about(request):
    return render(request, 'projects/about.html', {'title': 'About', 'mainUser': User.objects.filter(id=1).first()})


# Link Views
class LinkListView(ListView):
    model = Link
    def get_context_data(self, **kwargs):
        context = super(LinkListView, self).get_context_data(**kwargs)
        return context
    def get_queryset(self):
        try:
            proj = Project.objects.get(id=self.kwargs.get("project"))
            return Link.objects.filter(project=proj).order_by('title')
        except Exception:
            return Link.objects.order_by('project.title')

class LinkDetailView(DetailView):
    model = Link
    def get_context_data(self, **kwargs):
        context = super(LinkDetailView, self).get_context_data(**kwargs)
        context['cssFiles'] = {'projects/css/link-detail.css'}
        context['mainUser'] = User.objects.filter(id=1).first()
        return context

class LinkCreateView(LoginRequiredMixin, CreateView):
    model = Link
    fields = ['title', 'url', 'project']
    def form_valid(self, form):
        form.instance.author = self.request.user
        domain = urlparse(form.instance.url).netloc
        t = domain.split('.')[1]
        form.instance.platform = t.toUpperCase()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['mainUser'] = User.objects.filter(id=1).first()
        return context

class LinkUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Link
    fields = ['title', 'url', 'project']
    def form_valid(self, form):
        form.instance.author = self.request.user
        domain = urlparse(form.instance.url).netloc
        t = domain.split('.')[1]
        form.instance.platform = t.toUpperCase()
        return super().form_valid(form)
    def test_func(self):
        link = self.get_object()
        return self.request.user == link.author
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['mainUser'] = User.objects.filter(id=1).first()
        return context

class LinkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Link
    success_url = '/'
    def test_func(self):
        link = self.get_object()
        return self.request.user == link.author
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['mainUser'] = User.objects.filter(id=1).first()
        return context

## Views for individual Projects
def accentureJobSearch(request):
    context = {
        'jobs' : helperFunctions.getAccentureJobs(),
        'countries' : helperFunctions.getCountryName(),
        'languages' : helperFunctions.getLanguageName(),
        'mainUser': User.objects.filter(id=1).first(),
    }
    return render(request, 'projects/project/accentureJobSearch.html', context)