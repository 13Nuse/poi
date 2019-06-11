from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.base, name='base'),
    path('login', LoginView.as_view(template_name='user/login.html')),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/changepassword/', views.change_password, name='change_password'),
    path('logout', LogoutView.as_view(template_name='user/logout.html')),

    # employee
    path('create-employee', views.create_employee, name='create_employee'),
    path('edit-employee/<id>', views.edit_employee, name='edit_employee'),
    path('view-employee', views.view_employee, name='view_employee'),

    # inventory
    path('inventory-overview', views.inventory_overview, name='inventory-overview'),
    path('inventory-adjustment', views.inventory_adjustment, name='inventory_adjustment'),

    # sales
    path('projected-sales', views.projected_sales, name='projected-sales'),
    path('edit-projected-sales/<id>', views.edit_projected_sales, name='edit-projected-sales')

]
