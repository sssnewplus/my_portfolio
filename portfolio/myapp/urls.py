from django.urls import path 
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('blog-home/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('milky-way/', views.milky_way, name='milky_way'),
    # path('send-whatsapp/', views.send_whatsapp, name='send_whatsapp'),
]