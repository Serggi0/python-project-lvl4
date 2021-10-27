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
    path('create/', views.create, name='create'),  # https://youtu.be/QK4qbVyY7oU?t=114
    # страница редактирования пользователя:
    path('<int:user_id>/update/', views.update_user, name='update_user'),
    # страница удаления пользователя:
    path('<int:user_id>/delete/', views.delete_user, name='delete_user'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ! настройка статических файлов