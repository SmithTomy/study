from django.contrib import admin
from django.urls import include,path

urlpatterns = [
        path('lib/',include('lib.urls')),
        path('admin/',admin.site.urls),
        ]
