from django.http import response
from django.test import TestCase, RequestFactory

from django.contrib.auth import get_user_model

from users.views import CreateUser, UpdateUser
from statuses.views import CreateStatus

from .models import *


class UserTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name='Ivan',
            last_name='Ivanov',
            username='ivanich'
        )

    def test_create_user(self):
        self.assertIn(self.user, User.objects.all())
        self.assertIn(self.user.first_name, User.objects.get(pk='1').first_name)
        self.assertIn(self.user.full_name, User.objects.get(pk='1').full_name)

    def test_response_user(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        response = CreateUser.as_view()(request)
        self.assertEqual(response.status_code, 200)


    def test_response_update_user(self):
        factory = RequestFactory()
        request = factory.post('')
        request.user = self.user
        response = UpdateUser.as_view()(request, pk='1')
        self.assertEqual(response.status_code, 200)

class StatusTestCase(TestCase):
    def setUp(self):
        self.status = Status.objects.create(
            name='in working',
        )

    def test_create_status(self):
        self.assertIn(self.status, Status.objects.all())
