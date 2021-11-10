from django import urls
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tasks import views

app_name = 'tasks' #! установка пространства имен приложения
urlpatterns = [

# страница задач:
    path('', views.TasksView.as_view(), name='tasks'),
    path('create/', views.CreateTask.as_view(), name='create_task'),
    path('<int:pk>/', views.TaskView.as_view(), name='view_task'),
    path('<int:pk>/update/', views.UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete/', views.DeleteTask.as_view(), name='delete_task'),
]
