from django.contrib import admin

from django.urls import path, include
# from notes.api import api
from django.conf import settings
from django.conf.urls.static import static

 

urlpatterns = [

 path('admin/', admin.site.urls),

#  path("api/", api.urls),

 path('', include('apps.microapps.stickynotes.urls', namespace="stickynotes")),
 path('api/', include('api.urls'))

]

urlpatterns += static(settings.STATIC_URL, 
document_root=settings.STATIC_ROOT)
