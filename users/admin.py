from django.contrib import admin
from users.models import *


admin.site.register([User, Task, Label])
# ! выносит модель в панель администратора
