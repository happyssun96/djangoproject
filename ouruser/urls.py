from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register ,name = 'register'),
    path('login/', views.login, name = 'login'),
    path('home/', views.logined ,name = 'logined'),
    path('logout/', views.logout, name = 'logout'),
    path('newblog/', views.create, name='newblog'),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('', views.read, name="home"),
    path('<int:blog_id>/', views.detail, name='detail'),

]
