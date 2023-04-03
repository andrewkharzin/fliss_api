import graphene
from graphene import Argument, Field, ID, ObjectType, Schema
from graphene_django.filter import DjangoFilterConnectionField
from apps.microapps.stickynotes.models import Note
from .types import NoteType
from .filters import *
from .mutations import *


class Query(ObjectType):
    notes = DjangoFilterConnectionField(NoteType, filterset_class=NoteFilter)
    note = Field(NoteType, id=Argument(ID, required=True))
    def resolve_notes(root, info, **kwargs):
        return Note.objects.all()
    def resolve_note(root, info, **kwargs):
        return Note.objects.get(id=kwargs.get('id'))
    
class Mutation(ObjectType):
    note_create = NoteCreate.Field()
    note_delete = NoteDelete.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)