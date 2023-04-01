from django.urls import path, include

urlpatterns = [

 path('stickynotes/', include('api.microapps.stickynotes.urls'))

]