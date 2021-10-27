from django.contrib import admin
from users.models import Users


admin.site.register(Users)
# ! вынести модель в панель администратора