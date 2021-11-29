from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from tasks.models import Task
from labels.models import Label
from statuses.models import Status


class TaskTestCase(TestCase):

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

        l1 = Label(name='label_name')
        l1.save()
        s1 = Status(name='status_name')
        s1.save()
        self.task = Task(
            name='task_name',
            author=self.user1,
            # executor=self.user2,
            status=Status.objects.get(pk=1),
        )
        self.task.save()
        self.task.label.add(l1)

    # если вкл: django.db.models.deletion.ProtectedError:
    # Очистка после каждого метода
    # def tearDown(self):
    #     self.user1.delete()
    #     self.user2.delete()
    #     self.task.delete()
        # self.task2.delete()

    def test_create_task(self):
        self.client.login(username='ivanich', password='123test098')
        l2 = Label(name='label_name2')
        l2.save()
        s2 = Status(name='status_name2')
        s2.save()
        self.task = Task(
            name='task_create',
            author=self.user1,
            executor=self.user2,
            status=Status.objects.get(pk=2),
        )
        self.task.save()
        self.task.label.add(l2)
        self.assertIn(self.task, Task.objects.all())
        self.assertIn('task_create', Task.objects.get(pk='2').name)

    def test_task_view_logout(self):
        # более наглядный, чем следующий тест
        self.client.logout()
        response = self.client.get(
            '/logout/'
        )
        response = self.client.get(reverse('tasks:tasks'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')  # переадресация

    def test_task_no_view(self):
        response = self.client.get(reverse('tasks:tasks'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')  # переадресация

    def test_update_task(self):
        # self.client.login(username='ivanich', password='123test098')
        self.client.login(username='masha', password='098test!@#')
        response = self.client.post(
            reverse('tasks:update_task', kwargs={'pk': 1}), {
                'name': 'task_update',
                'description': 'description',
                'executor': 2,
                'status': 1,
                'label': 1
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual('task_update', Task.objects.get(pk=1).name)

    def test_delete_task(self):
        self.client.login(username='ivanich', password='123test098')
        response = self.client.post(
            reverse('tasks:delete_task', args='1')
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=1))  # отсутствует pk=1

    # def test_delete_non_own_task(self):
    #     self.client.login(username='masha', password='098test!@#')
    #     # self.client.login(username='ivanich', password='123test098')
    #     try:
    #         self.client.post(
    #             reverse('tasks:delete_task', kwargs={'pk': 1})
    #             )
    #         self.assertFalse(Task.objects.filter(pk=1))
    #     except ProtectedError as e:
    #         self.assertEqual(user_messages.ERROR_MESSAGE_DELETED_TASK, e)
    #         # self.assertTrue(Task.objects.filter(pk=1))  # pk=1 не удален

    # def test_delete_non_own_task(self):
    #     self.client.login(username='masha', password='098test!@#')
    #     # self.client.login(username='ivanich', password='123test098')
    #     response = self.client.post(
    #         reverse('tasks:delete_task', kwargs={'pk': 1})
    #         )
    #     # self.assertEqual(response.status_code, 302)
    #     self.assertTrue(Task.objects.filter(pk=1))  # pk=1 не удален
