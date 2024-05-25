from django.urls import path
from . import views
urlpatterns = [
    path('tasks/show', views.showTasks, name="showTasks"),
    path('task/show/<str:pk>/', views.showTask, name="showTask"),

    path('task/create', views.createTask, name="createTask"),
    path('task/edit/<str:pk>', views.editTask, name="editTask"),
    path('task/delete/<str:pk>', views.deleteTask, name="deleteTask"),
]