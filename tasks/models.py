from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from statuses.models import Status
from labels.models import Label


class Task(models.Model):
    name = models.CharField(
        unique=True, max_length=250,
        verbose_name=_('Name')
    )
    description = models.TextField(
        blank=True,
        verbose_name=_('Description'),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        related_name='author',
        verbose_name=_('Author')
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executor',
        null=True,
        blank=True,
        verbose_name=_('Executor')
    )
    labels = models.ManyToManyField(
        Label,
        blank=True,
        verbose_name=_('Labels')
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=_('Status')
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Create date')
    )

    def __str__(self) -> str:
        return self.name
