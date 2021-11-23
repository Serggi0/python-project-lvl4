from django.urls import path

from users import views

app_name = 'users'  # ! установка пространства имен приложения
urlpatterns = [
    path('', views.UsersView.as_view(), name='users'),

    # страница регистрации нового пользователя (создание):
    path('create/', views.CreateUser.as_view(), name='create_user'),
    # https://youtu.be/QK4qbVyY7oU?t=114

    # страница редактирования пользователя:
    path('<int:pk>/update/', views.UpdateUser.as_view(), name='update_user'),

    # страница удаления пользователя:
    path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete_user'),
]
