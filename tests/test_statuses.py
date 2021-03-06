from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from statuses.models import Status


class StatusTestCase(TestCase):

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

        self.status1 = Status(name='status_name1')
        self.status1.save()
        self.status2 = Status(name='status_name2')
        self.status2.save()

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.status1.delete()
        self.status2.delete()

    def test_create_status(self):
        self.client.login(username='masha', password='098test!@#')
        response = self.client.post(
            reverse('statuses:create_status'),
            {'name': 'status_create'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.get(name='status_create'))

    def test_update_status(self):
        self.client.login(username='ivanich', password='123test098')
        response = self.client.post(
            reverse('statuses:update_status', args='1'), {
                'name': 'status_update',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual('status_update', Status.objects.get(pk=1).name)

    def test_delete_status(self):
        self.client.login(username='ivanich', password='123test098')
        response = self.client.post(
            reverse('statuses:delete_status', args='1')
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Status.objects.filter(pk=1))

    def test_status_view_logout(self):
        self.client.logout()
        response = self.client.get('/logout/')
        response = self.client.get(reverse('statuses:statuses'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')

    def test_status_no_view(self):
        response = self.client.get(reverse('statuses:statuses'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')
