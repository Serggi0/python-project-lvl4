from django.test import TestCase

from .models import *

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            first_name='Ivan',
            last_name='Ivanov',
            username='ivanich'
        )
        Statuses.objects.create(
            name='in working',
        )

    def test_user_create_status(self):
        pass