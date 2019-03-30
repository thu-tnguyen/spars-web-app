from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from django.http import HttpResponse
from pages.models import Project,Author


### All Template View classes 
class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Project, Author

class AboutPageView(TemplateView):
    template_name = 'about.html'
    model = Project, Author

class ResultPageView(TemplateView):
    template_name = 'result.html'
    model = Project, Author

class ProjectPageView(TemplateView):
    template_name = 'projects.html'
    model = Project, Author

class AlumniTreePageView(TemplateView):
    template_name = 'alumni_tree.html'
    model = Project, Author

class ContactPageView(TemplateView):
    template_name = 'contact.html'
    model = Project, Author

### ???
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        projects = Project.objects.filter(title__icontains=q)            
        return render(request, 'result.html', {'projects': projects, 'query': q})

def project_url_link(request, project_title):
    q = get_object_or_404(Project, title=project_title)
    return render_to_response('projects.html', context, RequestContext(request))