from django.urls import path 
from . import views 
urlpatterns = [ 
    path('',views.dashboard, name='dashboard'),
    path('students/<uuid:id>/',views.admin_student_dashboard, name='admin_student_dashboard'),
    path('student/change-picture/', views.changePic, name='profpic-change'),
]