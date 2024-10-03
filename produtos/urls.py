from django.contrib import admin
from django.urls import path
from produtos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_products/', views.get_products, name='list_products')
]
