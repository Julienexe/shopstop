from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('',views.home, name="home"),
    path('business/register/', views.business_register, name='business_register'),
    path('menu/manage/', views.menu_management, name='menu_management'),
    path('service/manage/', views.service_management, name='service_management'),
    path('manage_business/<business_id>', views.business_management, name = 'management')
]