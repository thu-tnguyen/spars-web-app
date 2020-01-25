from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.urls import reverse
from pages.models import Project, Author

from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Project, Author

class BrowseView(TemplateView):
    template_name = 'browse.html'
    #queryset = Project.objects.all()

    # filter_backends = (OrderingFilter, SearchFilter)
    # filter_class = ResultFilter
    # ordering_fields = ('year', 'title', 'author', 'mentor')
    # search_fields = ('title', 'author', 'mentor', 'tagline', 'year')

    def get_queryset(self):
        if 'q' in self.GET and self.GET['q']:
            q = self.GET['q']
            s = self.GET['s']
        else:
            q = ''
            s = self.GET['s']
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
        cat = self.GET.get('cat', '').split(',')
        if (cat != ['']): 
            temp = projects & Project.objects.filter(tagline__icontains=cat[0])
            for c in cat:
                temp = temp | (projects & Project.objects.filter(tagline__icontains=c))
            projects = temp
        return render(self, 'ajax_search.html', {'projects': projects})
    
    # def get_context_data(self, **kwargs):
    #     context = super(BrowseListView, self).get_context_data(**kwargs)
    #     search_query = self.get_queryset()
    #     return context


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
    
    # else:
    #     return render(request, 'result.html')

    # if 'sort_by' in request.GET and request.GET['sort_by']:
    #     sort_by = request.GET.get('sort_by', '')
    # else:
    #     sort_by = 'title'

    # Project.objects.order_by(sort_by)
    
    cat = request.GET.get('cat', '').split(',')
    if (cat != ['']): 
        temp = projects & Project.objects.filter(tagline__icontains=cat[0])
        for c in cat:
            temp = temp | (projects & Project.objects.filter(tagline__icontains=c))
        projects = temp
    return render(request, 'ajax_search.html', {'projects': projects})
        

    
