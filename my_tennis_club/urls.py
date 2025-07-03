from django.contrib import admin
from django.urls import path, include
from members import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('', views.main, name='main'),  # This line is for the root URL
]