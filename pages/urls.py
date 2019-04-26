from django.urls import path, include
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    url(r'^result/$', views.search, name='result'),
    path('projects/<uuid:ext_id>/', views.ProjectDetailView.as_view(), name='rsprojects'),
    path('alumni_tree/', views.AlumniTreePageView.as_view(), name='alumni_tree'),
    path('browse/', views.BrowseListView.as_view(), name='browse'),
] 