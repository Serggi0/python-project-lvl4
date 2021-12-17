from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    full_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name=_('Full name'))

    def save(self, *args, **kw):
        self.full_name = '{0} {1}'.format(self.first_name, self.last_name)
        super(User, self).save(*args, **kw)

    def __str__(self):
        return self.full_name
