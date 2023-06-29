#from django.contrib import admin
#from django.urls import path
#from file_upload import views

#urlpatterns = [
 #  path('',views.index,name="index")
#]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('',include('file_upload.urls')),
]