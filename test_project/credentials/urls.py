from django.urls import path
from .import views
app_name='credentials'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout,name='logout'),
    path('update/<int:id>/',views.update,name='update_user'),
    path('delete/<int:id>/',views.delete,name='delete_user'),
    path('add/>/',views.add,name='add_user'),
    path('search/', views.SearchResult, name='SearchResult'),
    path('adminlogin/',views.admin_login, name='admin_login'),
    path('admin/',views.admin, name='admin')
]