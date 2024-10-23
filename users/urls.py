from django.contrib import admin
from django.urls import path
from users.views import login, register, logout


urlpatterns = [
    path('admin/', admin.site.urls),   
    path('login', login, name='login'), 
    path('register', register, name='register'), 
    path('logout', logout, name='logout'),
] 
