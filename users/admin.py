from django.contrib import admin
from users.models import User


admin.site.register(User)
# ! выносит модель в панель администратора
