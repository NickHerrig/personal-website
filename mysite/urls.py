from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('essays/', include('essays.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
