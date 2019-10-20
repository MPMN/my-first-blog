from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('W3', views.W3, name='W3'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]