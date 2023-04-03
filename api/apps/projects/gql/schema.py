import graphene
from graphene import Argument, Field, ID, ObjectType, Schema
from graphene_django import DjangoObjectType
from django_filters import FilterSet
from graphene import List, String, Int
from graphene_django.filter import DjangoFilterConnectionField
from apps.projects.models.project  import Project
# from apps.projects.models.document  import Document
# from apps.projects.models.note import Note
from .filters import *
from .types import *
from .mutations import ProjectCreate, ProjectDelete


class Query(ObjectType):
    # project queries
    projects = DjangoFilterConnectionField(ProjectType, filterset_class=ProjectFilter)
    project = Field(ProjectType, id=Argument(ID, required=True))
    # # documents queries     
    # documents = graphene.List(DocumentType)
    # # notes queries 
    # notes = graphene.List(NoteType)

    # # customers queries
    # customers = graphene.List(CustomerType)
    # customer = Field(CustomerType, id=Argument(ID, required=True))

    # Projects resolver

    def resolve_projects(self, info):
        return Project.objects.all()
    
    def resolve_project(self, info, **kwargs):
        return Project.objects.get(id=kwargs.get('id'))
    
    # # Documents resolver

    # def resolve_documents(self, info):
    #     return Document.objects.all()
    
    # # Notes resolver

    # def resolve_notes(self, info):
    #     return Note.objects.all()
    
    # # Customers resolver

    # def resolve_customers(self, info):
    #     return Customer.objects.all()
    
    # def resolve_customer(self, info, **kwargs):
    #     return Customer.objects.get(id=kwargs.get('id'))
    
class Mutation(ObjectType):
    project_create = ProjectCreate.Field()
    project_delete = ProjectDelete.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
