from django.urls import path 
from . import views 
urlpatterns = [ 
    path('gemadmin/', views.index, name='gemadmin'),
    path('adminchangepic/<str:user>/', views.adminchangePic, name="adminchangepic"),
    path('search/', views.search, name='search')
]