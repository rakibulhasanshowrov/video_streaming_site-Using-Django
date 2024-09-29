from django.urls import path
from user_handle import views
app_name='user_handle'
urlpatterns=[
  path('',views.homepage,name='homepage'),
  # path('signup/',views.sign_up,name='signup'),
  path('login/',views.login_user ,name='login_user'),
  # path('logout/',views.logout_user ,name='logout'),
  # path('profile/',views.user_profile ,name='profile'),
  
]