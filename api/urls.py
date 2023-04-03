from django.urls import path, include

urlpatterns = [

  path('', include("api.microapps.stickynotes.rest.urls"))

]