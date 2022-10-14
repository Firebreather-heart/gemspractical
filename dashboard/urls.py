from django.urls import path 
from . import views 
urlpatterns = [ 
    path('',views.dashboard, name='dashboard'),
    path('<uuid:pk>/',views.admin_student_dashboard, name='admin_student_dashboard'),
    path('profpic-change/', views.changePic, name='profpic-change'),
]