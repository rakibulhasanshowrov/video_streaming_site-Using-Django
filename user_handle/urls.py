from django.urls import path
from user_handle import views
app_name='user_handle'
urlpatterns=[
  
  path('signup/',views.create_user,name='signup'),
  path('login/',views.login_user ,name='login_user'),
  path('logout/',views.logout_user ,name='logout_user'),
  path('profile/',views.userProfile ,name='profile'),
  
]