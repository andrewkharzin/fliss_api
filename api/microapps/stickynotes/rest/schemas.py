from ninja import Schema, ModelSchema

from datetime import date

from apps.microapps.stickynotes.models import StickyNote



class CategoryIn(Schema):

    title: str

    description: str


class CategoryOut(Schema):

    id: int

    title: str

    description: str    

    created: date

  


class StickyNoteIn(ModelSchema):

    class Config:

        model = StickyNote

        model_fields = ['title', 'category']


class StickyNoteUpd(ModelSchema):

    class Config:

        model = StickyNote

        model_fields = ['id', 'completed']


class StickyNoteOut(ModelSchema):

    class Config:

        model = StickyNote

        model_fields = ['id','title', 'category', 'created', 
'completed']
