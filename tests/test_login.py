from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import authenticate, get_user_model


class LoginTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            first_name='Ivan',
            last_name='Ivanov',
            username='ivanich',
            password='123test098'
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct_username(self):
        user = authenticate(
            username='ivanich',
            password='123test098'
        )
        self.assertTrue(user is not None and user.is_authenticated)

    def test_user_login(self):
        self.client.login(username='ivanich', password='123test098')
        response = self.client.get(reverse('users:users'))
        self.assertEqual(str(response.context['user']), 'Ivan Ivanov')
        # Проверка что пользователь залогинился

    def test_wrong_username(self):
        user = authenticate(
            username='wrong',
            password='123test098'
        )
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(
            username='ivanich',
            password='wrong'
        )
        self.assertFalse(user is not None and user.is_authenticated)

    def test_login_redirect(self):
        response = self.client.post(
            '/login/', {
                'username': 'ivanich',
                'password': '123test098'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        # ! self.client — HTTP-клиент тестовой библиотеки Django

    def test_logout_redirect(self):
        self.client.logout()
        response = self.client.get(
            '/logout/'
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
