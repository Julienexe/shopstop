from django.urls import path
from . import views

urlpatterns = [
    path('business/register/', views.business_register, name='business_register'),
    path('menu/manage/', views.menu_management, name='menu_management'),
    path('service/manage/', views.service_management, name='service_management')
]