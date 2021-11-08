from django.contrib import admin
from users.models import *


admin.site.register([User, Task, Status, Label])
# ! выносит модель в панель администратора
