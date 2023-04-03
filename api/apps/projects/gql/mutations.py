# back/gql/notes/mutations.py
import graphene
from graphene import Boolean, Field, ID, InputObjectType, Mutation, String
from rest_framework import serializers
from apps.projects.models.project import Project
# from apps.projects.models.document import Document
# from apps.projects.models.note import Note
from .types import ProjectType
from apps.customers.models.customer import Customer
from pytils.translit import slugify
from .utils import generate_unique_slug


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'description',
        )


class ProjectInputType(InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()
    # customer_id = graphene.ID(required=True)


# class ProjectCreate(Mutation):
#     class Arguments:
#         input = ProjectInputType(required=True)

#     project = Field(ProjectType)

#     @classmethod
#     def mutate(cls, root, info, **data):
#         customer_id = input.pop('customer_id')
#         customer = Customer.objects.get(id=customer_id)
#         serializer = ProjectSerializer(data=data.get('input'))
#         serializer.is_valid(raise_exception=True)

#         return ProjectCreate(project=serializer.save())
    

# class ProjectCreate(graphene.Mutation):
#     class Arguments:
#         project_data = ProjectInputType(required=True)

#     project = graphene.Field(lambda: ProjectType)

#     def mutate(self, info, project_data):
#         customer_id = project_data.pop('customer_id')
#         customer = Customer.objects.get(id=customer_id)
#         project = Project(customer=customer, **project_data)
#         project.save()

#         return ProjectCreate(project=project)


class ProjectCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        # customer_id = graphene.Int(required=True)

    project = graphene.Field(ProjectType)

    def mutate(self, info, name, description, customer_id):
        # customer = Customer.objects.get(pk=customer_id)
        slug = generate_unique_slug(Project, slugify(name))
        project = Project(name=name, description=description, slug=slug)
        project.save()
        return ProjectCreate(project=project)


# class ProjectDelete(Mutation):
#     class Arguments:
#         id = ID(required=True)

#     ok = Boolean()

#     @classmethod
#     def mutate(cls, root, info, **data):
#         note = Project.objects.get(id=data.get('id'))
#         note.delete()

#         return ProjectDelete(ok=True)
    
class ProjectDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = Boolean()

    project = graphene.Field(ProjectType)

    def mutate(self, info, id):
        project = Project.objects.get(pk=id)
        project.delete()
        return ProjectDelete(ok=True)