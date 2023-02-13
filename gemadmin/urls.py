from django.urls import path 
from . import views 
urlpatterns = [ 
    path('gemadmin/', views.index, name='gemadmin'),
    path('gemadmin/adminchangepic/<str:user>/', views.adminchangePic, name="adminchangepic"),
    path('gemadmin/search/', views.search, name='search'),
    path('gemadmin/<int:id>/make_payment/', views.make_payments, name='make_payment'),
    path('gemadmin/index/<str:arg>/', views.get_student_by_class, name='student_by_class')
]