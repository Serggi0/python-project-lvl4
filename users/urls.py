from django import urls
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users import views

app_name = 'users' #! установка пространства имен приложения
urlpatterns = [
    # страница со списком всех пользователей:
    path('', views.UsersView.as_view(), name='users'),

    # страница регистрации нового пользователя (создание):
    path('create/', views.CreateUser.as_view(), name='create'),  # https://youtu.be/QK4qbVyY7oU?t=114

    # страница редактирования пользователя:
    path('<int:pk>/update/', views.UpdateUser.as_view(), name='update_user'),

    # страница удаления пользователя:
    path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete_user'),

    # страница статусов:
    path('statuses/', views.StatusesView.as_view(), name='statuses'),
    path('statuses/create', views.CreateStatus.as_view(), name='create_status'),
    path('statuses/<int:pk>/update/', views.UpdateStatus.as_view(), name='update_status'),
    path('statuses/<int:pk>/delete/', views.DeleteStatus.as_view(), name='delete_status'),

    # страница задач:
    path('tasks/', views.TaskView.as_view(), name='tasks'),
    path('tasks/create', views.CreateTask.as_view(), name='create_task'),
    path('tasks/<int:pk>/update/', views.UpdateTask.as_view(), name='update_task'),
    path('tasks/<int:pk>/delete/', views.DeleteTask.as_view(), name='delete_task'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ! настройка статических файлов