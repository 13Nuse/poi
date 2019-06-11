from django.urls import path
from user import views


urlpatterns = [
    path('', views.base, name='base'),
]
