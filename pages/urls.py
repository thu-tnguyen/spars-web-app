from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    url(r'^result/$', views.search, name='result'),
    path('projects/<uuid:ext_id>/', views.ProjectPageView.as_view(), name='rsprojects'),
    path('alumni_tree/', views.AlumniTreePageView.as_view(), name='alumni_tree'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
] 