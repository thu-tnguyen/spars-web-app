import django_filters
from pages.models import Project,Author


class ResultListFilter(django_filters.FilterSet):
  class Meta:
    model = Project
    fields = ['title', 'division', 'mentor', 'year', 'presentation_format',] 
    order_by = ['pk']