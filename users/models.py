from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    famaly_name = models.CharField(max_length=150)
    nick_name = models.CharField(unique=True, max_length=100)
    # task_id = 
    create_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.nick_name()


class Statuses(models.Model):
    name = models.CharField(unique=True, max_length=100)
    create_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name


class Tags(models.Model):
    name = models.CharField(unique=True, max_length=100)
    create_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name


class Tasks(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    executor_id = models.OneToOneField(Users, on_delete=models.PROTECT)
    status_id = models.OneToOneField(Statuses, on_delete=models.PROTECT)
    tag_id = models.OneToOneField(Tags, on_delete=models.PROTECT)
    create_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name



