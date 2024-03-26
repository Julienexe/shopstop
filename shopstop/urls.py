from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.home, name="home"),
    path('shop/', views.shop, name= 'shop'),
    #product page
    path('detail/<item_id>', views.product_detail, name = 'prod-detail'),
    #add item
    path('add-item/', views.add_item, name = 'add-item'),
    path('business/register/', views.business_register, name='business_register'),
    path('menu/manage/', views.menu_management, name='menu_management'),
    path('service/manage/', views.service_management, name='service_management'),
    path('manage_business/<business_id>', views.business_management, name = 'management'),
    path('about/', views.about, name='about'),
    path('business-profile/', views.business_profile, name = 'business-profile'),
    #business form
    path('business_form/', views.create_business, name = 'create_business')
    
]