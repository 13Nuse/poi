from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('user.urls')),
    path('user/', include('user.urls')),
    path('recipe/', include('recipe.urls')),
    path('admin/', admin.site.urls),
]
