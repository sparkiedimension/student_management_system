from django.urls import path

from Student import views




urlpatterns = [
    path('nith/', views.index, name='index'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('analytics/', views.staffguidelines, name='analytics'),
    
    
]