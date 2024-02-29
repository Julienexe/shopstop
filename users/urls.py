from django.urls import path
from . import views

app_name = "users"
urlpatterns= [
    # 用户登录
    path('login/', views.user_login, name='user_login'),
    #signup
    path('signup',views.signup,name='signup'),
]