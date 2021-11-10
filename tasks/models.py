from django.db import models
from django.urls.base import reverse
from django.utils.translation import gettext_lazy as _
from users.models import User
from statuses.models import Status
from labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', null=True)
    # https://djangodoc.ru/3.1/ref/models/fields/#django.db.models.ForeignKey.related_name
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='executor', null=True, blank=True)
    label = models.ManyToManyField(Label, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name