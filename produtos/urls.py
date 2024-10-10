from django.contrib import admin
from django.urls import path
from produtos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('home/', views.get_products, name='home'),
    # path('register_product/', views.register_product, name='register_product'),
    path('petshop/', views.petshop, name='petshop'),
    path('banho_tosa/', views.banho_tosa, name='banho_tosa'),
    path('creche/', views.creche, name='creche'),
    path('respond_message/<str:message>', views.respond_message, name='respond_message'),
    path('check_storage/<int:currentValue>/<int:productId>', views.check_storage, name='check_storage'),
    path('cart', views.cart, name='cart')
] 


