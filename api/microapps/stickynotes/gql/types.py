from graphene_django import DjangoObjectType
from apps.microapps.stickynotes.models import Note


class NoteType(DjangoObjectType):
    class Meta:
        model = Note
        only_fields = (
            'id',
            'title',
            'description',
            'category',
            'completed',
            'created_at',
        )
        use_connection = True