import graphene
from graphene import Argument, Field, ID, ObjectType, Schema
from graphene_django import DjangoObjectType
from django_filters import FilterSet
from graphene import List, String, Int
from graphene_django.filter import DjangoFilterConnectionField
from apps.projects.models.project  import Project
# from apps.projects.models.document  import Document
# from apps.projects.models.note import Note
from apps.customers.models.customer import Customer
# from .filters import *



class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        # filterset_class = ProjectFilter
        fields = '__all__'
        use_connection = True

# class CustomerType(DjangoObjectType):
#     class Meta:
#         model = Customer
#         fields = '__all__'
#         use_connection = True

# class DocumentType(DjangoObjectType):
#     class Meta:
#         model = Document
#         fields = '__all__'
#         use_connection = True

# class NoteType(DjangoObjectType):
#     class Meta:
#         model = Note
#         fields = '__all__'
#         use_connection = True