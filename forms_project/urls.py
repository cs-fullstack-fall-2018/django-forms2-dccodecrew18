from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('', include('forms_app.urls')),
    path('memfood/'),include('MemphisRecipes.urls'), #this may be template
    path('admin/', admin.site.urls),
]