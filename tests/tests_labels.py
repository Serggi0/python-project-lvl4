from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from labels.models import Label


class LabelTestCase(TestCase):

    def setUp(self):
        # Установки запускаются перед каждым тестом
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

        self.label1 = Label(name='label_name1')
        self.label1.save()
        self.label2 = Label(name='label_name2')
        self.label2.save()

    def tearDown(self):
        # Очистка после каждого метода
        self.user1.delete()
        self.user2.delete()
        self.label1.delete()
        self.label2.delete()

    def test_create_label(self):
        self.label3 = Label(name='label_create')
        self.label3.save()
        self.assertIn(self.label3, Label.objects.all())
        self.assertIn('label_create', Label.objects.get(pk='3').name)

    def test_labels_view_logout(self):
        # более наглядный, чем следующий тест
        self.client.logout()
        response = self.client.get(
            '/logout/'
        )
        response = self.client.get(reverse('labels:labels'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')  # переадресация

    def test_labels_no_view(self):
        response = self.client.get(reverse('labels:labels'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')  # переадресация

    def test_update_label(self):
        self.client.login(username='masha', password='098test!@#')
        response = self.client.post(
            reverse('labels:update_label', kwargs={'pk': 1}), {
                'name': 'label_update',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual('label_update', Label.objects.get(pk=1).name)

    def test_delete_label(self):
        self.client.login(username='ivanich', password='123test098')
        response = self.client.post(
            reverse('labels:delete_label', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Label.objects.filter(pk=1))  # отсутствует
