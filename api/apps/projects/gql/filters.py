import graphene
from django_filters import FilterSet
from django.db.models import Q
import django_filters
from apps.projects.models.project import Project

# class ProjectFilter(django_filters.FilterSet):
#     search = django_filters.CharFilter(method='filter_search')
#     class Meta:
#         model = Project
#         fields = ()
#     def filter_search(self, queryset, name, value):
#         return queryset.filter(
#             Q(name__icontains=value)
#         )
    
class ProjectFilter(FilterSet):
    search = django_filters.CharFilter(method='filter_search')
    class Meta:
        model = Project
        fields = [
            'name',
        ]
        filter_fields = {
            'name': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node, )