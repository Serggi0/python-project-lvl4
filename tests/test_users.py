from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model

from users.views import CreateUser, UpdateUser
from users.models import User


class UserTestCase(TestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            first_name='Ivan',
            last_name='Ivanov',
            username='ivanich',
            password='123test098'
        )
        self.user1.save()

        self.user2 = get_user_model().objects.create_user(
            first_name='Masha',
            last_name='Petrova',
            username='masha',
            password='098test!@#'
        )
        self.user2.save()

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()

    def test_create_user(self):
        self.assertIn(self.user1, User.objects.all())
        self.assertIn('Ivan', User.objects.get(pk='1').first_name)
        self.assertIn('Ivanov', User.objects.get(pk='1').last_name)

    def test_users_view(self):
        self.client.login(username='ivanich', password='123test098')
        response = self.client.get(reverse('users:users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')

    def test_response_user(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user1
        response = CreateUser.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_view_update_user(self):
        factory = RequestFactory()
        request = factory.post('')
        request.user = self.user1
        response = UpdateUser.as_view()(request, pk='1')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        self.client.login(username='ivanich', password='123test098')
        response = self.client.post(reverse('users:update_user', args='1'), {
            'first_name': 'Ivan_update',
            'last_name': 'Ivanov',
            'username': 'ivanich_update',
            'password1': '123test098',
            'password2': '123test098',
        }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual('Ivan_update', User.objects.get(pk=1).first_name)
        self.assertEqual('ivanich_update', User.objects.get(pk=1).username)

    def test_delete_user(self):
        self.client.login(username='ivanich', password='123test098')
        response = self.client.post(reverse('users:delete_user', args='1'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(pk=1))

    def test_delete_other_user(self):
        self.client.login(username='ivanich', password='123test098')
        self.client.post(reverse('users:delete_user', args='2'))
        self.assertTrue(User.objects.filter(pk=2))
