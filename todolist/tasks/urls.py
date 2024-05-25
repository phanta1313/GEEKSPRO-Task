from django.urls import path
from . import views
urlpatterns = {
    path('tasks/show', views.showTasks, name="ShowTasks"),
    path('task/show/<str:pk>/', views.showTask, name="showTask"),

    path('tasks/add', views.createTask, name="createTask"),
    path('tasks/edit', views.editTask, name="editTask"),
    path('tasks/add', views.deleteTask, name="deleteTask"),
}