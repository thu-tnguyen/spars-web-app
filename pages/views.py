from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.urls import reverse
from pages.models import Project, Author

from django.db.models import Q

class HomePageView(TemplateView):
    """View to display Home Page"""
    template_name = 'home.html'
    model = Project, Author

class BrowseView(TemplateView):
    """View to display Browse Page"""
    template_name = 'browse.html'
    def get_queryset(self):
        """Fetch queryset and pass to `ajax_search.html`. Taking in query, search-by terms,
        (optionally categories using Sidebar). Filter using `icontanins`."""
        return search(self)

class ProjectDetailView(DetailView):
    """View to display project details"""
    template_name = 'projects.html'
    context_object_name = 'project'
    model = Project
    
    # Read UUID into Slug Field to accomodate DetailView 
    slug_field = 'ext_id'
    slug_url_kwarg = 'ext_id'

def search(request):
    """Fetch queryset and pass to `ajax_search.html`. Taking in query, search-by terms,
    (optionally categories using Sidebar). Filter using `icontanins`."""
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        s = request.GET['s']
    else:
        q = ''
        s = request.GET['s']
        projects = Project.objects.filter(tagline__icontains=q)
    if s == 'all':
        title = Project.objects.filter(title__icontains=q)
        tagline = Project.objects.filter(tagline__icontains=q) 
        author = Project.objects.filter(author__full_name__icontains=q)
        mentor = Project.objects.filter(mentor__icontains=q)

        projects = title | tagline | author | mentor
    elif s == 'title':
        projects = Project.objects.filter(title__icontains=q)         
    elif s == 'author':
        projects = Project.objects.filter(author__full_name__icontains=q)         
    elif s == 'mentor':
        projects = Project.objects.filter(mentor__icontains=q)         
    elif s == 'tagline':
        projects = Project.objects.filter(tagline__icontains=q)  
    cat = request.GET.get('cat', '').split(',')
    if (cat != ['']): 
        temp = projects & Project.objects.filter(tagline__icontains=cat[0])
        for c in cat:
            temp = temp | (projects & Project.objects.filter(tagline__icontains=c))
        projects = temp
    return render(request, 'ajax_search.html', {'projects': projects.distinct()})
    
