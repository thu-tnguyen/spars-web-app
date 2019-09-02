from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.urls import reverse
from pages.models import Project, Author

from django.db.models import Q
from pages.serializers import ProjectSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters

class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Project, Author

class ResultFilter(FilterSet):
    title = filters.CharFilter('title')
    author = filters.CharFilter('author__full_name')
    mentor = filters.CharFilter('mentor')
    tagline = filters.CharFilter('tagline')
    year = filters.CharFilter('year')
    class Meta:
        model = Project
        fields = ('title', 'author', 'mentor', 'tagline', 'year')

class BrowseListView(ListView):
    model = Project
    serializer_class = ProjectSerializer
    template_name = 'browse.html'
    context_object_name = 'projects'
    #queryset = Project.objects.all()

    filter_backends = (OrderingFilter, SearchFilter)
    filter_class = ResultFilter
    ordering_fields = ('year', 'title', 'author', 'mentor')
    search_fields = ('title', 'author', 'mentor', 'tagline', 'year')

    def get_queryset(self):
        queryset = Project.objects.all()
        if 'q' in self.request.GET and self.request.GET['q']:
            q = self.request.GET.get('q')
            projects = queryset.filter(title__icontains=q) or queryset.filter(author__full_name__icontains=q) or queryset.filter(mentor__icontains=q) or queryset.filter(tagline__icontains=q)
        else:
            projects = queryset
        print('DEBUG:',projects)
        return projects
    
    # def get_context_data(self, **kwargs):
    #     context = super(BrowseListView, self).get_context_data(**kwargs)
    #     search_query = self.get_queryset()
    #     return context

class ResultListView(ListView):
    model = Project
    serializer_class = ProjectSerializer
    
    queryset = Project.objects.all()
    template_name = 'browser.html'

    filter_backends = (OrderingFilter, SearchFilter)
    filter_class = ResultFilter
    ordering_fields = ('year', 'title', 'author', 'mentor')
    search_fields = ('title', 'author', 'mentor', 'tagline', 'year')

    # def get_queryset(self):
    #     queryset = Project.objects.all()
    #     q = self.request.GET.get('q')
    #     s = self.request.GET.get('s')
    #     if s == 'all':
    #         projects = queryset.filter(title__icontains=q) and queryset.filter(author__full_name__icontains=q) and queryset.filter(mentor__icontains=q) and queryset.filter(tagline__icontains=q)
    #     elif s == 'title':
    #         projects = queryset.filter(title__icontains=q)         
    #     elif s == 'author':
    #         projects = queryset.filter(author__full_name__icontains=q)         
    #     elif s == 'mentor':
    #         projects = queryset.filter(mentor__icontains=q)         
    #     elif s == 'tagline':
    #         projects = queryset.filter(tagline__icontains=q)
    #     return projects
    
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
        projects = Project.objects.filter(Q(title__icontains=q) | Q(tagline__icontains=q) | Q(author__full_name__icontains=q) | Q(mentor__icontains=q))
    else:
        projects = Project.objects.all()
        return render(request, 'browse.html', {'projects': projects})
    return render(request, 'browse.html', {'projects': projects, 'query': q})
        

    


# def search(request):
#     if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#         s = request.GET['s']

#         if s == 'all':
#             projects = Project.objects.filter(title__icontains=q) or Project.objects.filter(tagline__icontains=q) or Project.objects.filter(author__full_name__icontains=q) or Project.objects.filter(mentor__icontains=q)
#         elif s == 'title':
#             projects = Project.objects.filter(title__icontains=q)         
#         elif s == 'author':
#             projects = Project.objects.filter(author__full_name__icontains=q)         
#         elif s == 'mentor':
#             projects = Project.objects.filter(mentor__icontains=q)         
#         elif s == 'tagline':
#             projects = Project.objects.filter(tagline__icontains=q)  
#         else:
#             projects = Project.objects.all()
#     else:
#         return render(request, 'result.html')

#     if 'sort_by' in request.GET and request.GET['sort_by']:
#         sort_by = request.GET.get('sort_by', '')
#     else:
#         sort_by = 'title'

#     Project.objects.order_by(sort_by)
#     return render(request, 'result.html', {'projects': projects, 'query': q, 'order_by': sort_by})
        

    
