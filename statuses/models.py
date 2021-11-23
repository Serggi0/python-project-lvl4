from django.db import models
from django.utils.translation import ugettext as _


class Status(models.Model):
    name = models.CharField(
        unique=True, max_length=100, verbose_name=_('Name')
    )
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Create date')
    )

    def __str__(self) -> str:
        return self.name
