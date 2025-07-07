from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    # path('', views.members, name='members'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('partner/', views.partner, name='partner'),
    path('test/', views.test, name='test'),
]
 
