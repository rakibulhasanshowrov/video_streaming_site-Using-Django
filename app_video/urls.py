from django.contrib import admin
from django.urls import path,include
from app_video import views 
app_name='app_video'
urlpatterns = [
    path('search/',views.vid_search,name='vid_search'),
    path('add_video/',views.add_video,name='add_video'),
    # path('',include('user_handle.urls')),
    # path('video/',include('app_video.urls')),  
    path('',views.homepage,name='homepage'),
]