from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    # path('', views.members, name='members'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('meri_tech/', views.meri_tech, name='meri_tech'),
    path('test/', views.test, name='test'),
]
 
