from django.contrib import admin
from users.models import User


admin.site.register(User)
# ! вынести модель в панель администратора