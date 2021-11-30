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
    # https://coderoad.ru/7681708/%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B3%D0%BE-%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8-%D0%B2-Django  # Noqa

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    #     name = ['update_user', 'logout']
    #     return reverse(name, kwargs={'user_id': self.pk})
    # централизованное управление 'user_id' в urls  и templates
    # https://youtu.be/CFO4aAsUuUk?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&t=732
