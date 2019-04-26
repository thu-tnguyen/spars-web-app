from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from pages.models import Project,Author


### All Template View classes 
class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Project, Author

class BrowseListView(ListView):
    model = Project
    template_name = 'browse.html'
    context_object_name = 'projects'
    ordering = ['-ext_id']

class ResultListView(ListView):
    model = Project
    template_name = 'result.html'
    context_object_name = 'projects'
    ordering = ['-ext_id']

    def get_queryset(self):
        q = self.request.GET.get('q')
        s = self.request.GET.get('s')

        if s == 'all':
            projects = Project.objects.filter(title__icontains=q) or Project.objects.filter(tagline__icontains=q) or Project.objects.filter(author__icontains=q) or Project.objects.filter(mentor__icontains=q)
        if s == 'title':
            projects = Project.objects.filter(title__icontains=q)         
        if s == 'author':
            projects = Project.objects.filter(author__icontains=q)         
        if s == 'mentor':
            projects = Project.objects.filter(mentor__icontains=q)         
        if s == 'tagline':
            projects = Project.objects.filter(tagline__icontains=q)  
        return projects
    
    def get_context_data(self, **kwargs):
        context = super(ResultListView, self).get_context_data(**kwargs)
        search_query = self.get_queryset()
        return context


class ProjectDetailView(DetailView):
    template_name = 'projects.html'
    context_object_name = 'project'
    model = Project
    
    # Read UUID into Slug Field to accomodate DetailView 
    slug_field = 'ext_id'
    slug_url_kwarg = 'ext_id'

class AlumniTreePageView(TemplateView):
    template_name = 'alumni_tree.html'
    model = Project, Author

class ContactPageView(TemplateView):
    template_name = 'contact.html'
    model = Project, Author


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        s = request.GET['s']
        sort_by = request.GET.get('sort_by', '')

        if s == 'all':
            projects = Project.objects.filter(title__icontains=q) or Project.objects.filter(tagline__icontains=q) or Project.objects.filter(author__icontains=q) or Project.objects.filter(mentor__icontains=q)

        if s == 'title':
            projects = Project.objects.filter(title__icontains=q)         
        if s == 'author':
            projects = Project.objects.filter(author__icontains=q)         
        if s == 'mentor':
            projects = Project.objects.filter(mentor__icontains=q)         
        if s == 'tagline':
            projects = Project.objects.filter(tagline__icontains=q)  
        
        Project.objects.order_by(sort_by)

        return render(request, 'result.html', {'projects': projects, 'query': q, 'order_by': sort_by})