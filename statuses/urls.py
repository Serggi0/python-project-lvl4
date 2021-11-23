from django.urls import path
from statuses import views


app_name = 'statuses'  # ! установка пространства имен приложения

urlpatterns = [

    # страница статусов:
    path(
        '', views.StatusesView.as_view(), name='statuses'
    ),
    path(
        'create/', views.CreateStatus.as_view(), name='create_status'
    ),
    path(
        '<int:pk>/update/', views.UpdateStatus.as_view(), name='update_status'
    ),
    path(
        '<int:pk>/delete/', views.DeleteStatus.as_view(), name='delete_status'
    ),
]
