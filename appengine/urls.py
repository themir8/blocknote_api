from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('api/v1/', include('main.urls')),
]
