
from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('employeedata/', views.data, name='employeedata'),
    path('delete/<int:id>', views.deleteme, name='deleteme'),
    path('edit/<int:id>', views.editme, name='editme'),
    path('logout/', views.loggout, name='logout'),


]





