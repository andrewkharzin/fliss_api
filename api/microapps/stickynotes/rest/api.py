from datetime import date

from typing import List

from ninja import NinjaAPI, Schema

from django.shortcuts import get_object_or_404

from apps.microapps.stickynotes import StickyNote, Category

from .schemas import StickyNoteIn, StickyNoteOut, StickyNoteUpd, CategoryIn, CategoryOut



api = NinjaAPI()



@api.post("/sticknotes", tags=['Заметки'])

def create_stickynote(request, payload: StickyNoteIn):

    data = payload.dict()

    category = Category.objects.get(id=data['category'])

    del data['category']

    note = StickyNote.objects.create(category=category, **data)

    return {"id": stickyote.id}


@api.post("/category", tags=['Категории'])

def create_category(request, payload: CategoryIn):

    category = Category.objects.create(**payload.dict())

    return {"id":category.id}    



@api.get("/stickynotes/{stickynote_id}", response=StickyNoteOut, tags=['Заметки'])

def get_stickynote(request, note_id: int):

    stickynote = get_object_or_404(StickyNote, id=stickynote_id)

    return stickynote


@api.get("/category/{category_id}", response=CategoryOut, 
tags=['Категории'])

def get_category(request, category_id: int):

    category = get_object_or_404(Category, id=category_id)

    return category


@api.get("/category", response=List[CategoryOut], 
tags=['Категории'])

def list_categories(request):

    categories = Category.objects.all()

    return categories   


@api.get("/stickynotes", response=List[StickyNoteOut], tags=['Заметки'])

def list_stickynotes(request):

    stickynotes = StickyNote.objects.all()

    return stickynotes



@api.patch("/stickynotes/{stickynote_id}", tags=['Заметки'])

def update_stickynote(request, stickynote_id: int, payload: StickyNoteUpd):

    stickynote = get_object_or_404(StickyNote, id=stickynote_id)

    for attr, value in payload.dict().items():

        setattr(stickynote, attr, value)

    stickynote.save()

    return {"success": True}


@api.put("/category/{category_id}", tags=['Категории'])

def update_category(request, category_id: int, payload: 
CategoryIn):

    category = get_object_or_404(Category, id=category_id)

    for attr, value in payload.dict().items():

        setattr(category, attr, value)

    category.save()

    return {"success": True}


@api.delete("/stickynotes/{stickynote_id}", tags=['Заметки'])

def delete_stickynote(request, stickynote_id: int):

    stickynote = get_object_or_404(StickyNote, id=stickynote_id)

    stickynote.delete()

    return {"success": True}


@api.delete("/category/{category_id}", tags=['Категории'])

def delete_category(request, category_id: int):

    category = get_object_or_404(Category, id=category_id)

    category.delete()

    return {"success": True}
