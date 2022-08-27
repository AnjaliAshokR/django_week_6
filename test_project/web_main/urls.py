from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('',views.welcome_page,name='welcome_page')
]