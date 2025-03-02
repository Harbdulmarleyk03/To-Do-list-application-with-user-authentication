from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('main/', views.main, name='main'),
    path('create_task/', views.add_task, name='task_create'),
    path('task/details/<int:task_id>', views.task_details, name='task_details'),
    path('task/update/<int:task_id>', views.task_update, name='task_edit'),
    path('task/delete/<int:task_id>', views.delete_view, name="task_delete"),
]
