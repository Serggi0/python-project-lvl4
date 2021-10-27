from django.db import models
from django.urls.base import reverse


class Users(models.Model):
    name = models.CharField(max_length=100)
    famaly_name = models.CharField(max_length=150)
    nick_name = models.CharField(unique=True, max_length=100)
    # task_id = 
    create_date = models.DateTimeField(auto_now_add=True)
    # self_task = models.BooleanField(default=True)

    def __str__(self):
        return self.nick_name

    def get_absolute_url(self):
        name = ['update_user', 'delete_user', 'logout']
        return reverse(name, kwargs={'user_id': self.pk})
    # централизованное управление 'user_id' в urls  и templates
    # https://youtu.be/CFO4aAsUuUk?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&t=732


class Statuses(models.Model):
    name = models.CharField(unique=True, max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Tags(models.Model):
    name = models.CharField(unique=True, max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Tasks(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    # user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='+', null=True)
    # https://djangodoc.ru/3.1/ref/models/fields/#django.db.models.ForeignKey.related_name
    executor_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    status_id = models.OneToOneField(Statuses, on_delete=models.PROTECT)
    tag_id = models.OneToOneField(Tags, on_delete=models.PROTECT)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name



