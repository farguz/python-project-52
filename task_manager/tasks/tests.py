from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.test import TestCase
from django.urls import reverse

from .models import Task

# Create your tests here.


class TasksTest(TestCase):

    fixtures = [
        'tasks.json',
        'users.json',
        'statuses.json',
        ]
    
    def setUp(self): 
        self.task_list_url = reverse('task_list')

        self.User = get_user_model()
        self.admin_user = self.User.objects.get(pk=1)
        self.client.force_login(self.admin_user) 

        self.test_task = Task.objects.get(pk=19)

    def test_task_list(self):
        response = self.client.get(self.task_list_url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('tasks', response.context)

        tasks = response.context['tasks']
        self.assertTrue(len(tasks) > 0)

    def test_task_create(self):
        create_url = reverse('task_create')

        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)

        new_task = {
            "name": "ppokpokpok",
            "description": "opkooiopsaads",
            "status": 9,
            "creator": 1,
            "executor": 14,
            }
        response = self.client.post(create_url, new_task)
        self.assertEqual(response.status_code, 302)  # 302 redirect

        response = self.client.get(self.task_list_url)
        self.assertContains(response, 'ppokpokpok')  # html
        self.assertTrue(Task.objects.filter(name='ppokpokpok').exists())  # database

    def test_task_update(self):
        update_url = reverse('task_update', kwargs={'pk': self.test_task.pk})

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        task_dict = model_to_dict(
            self.test_task,
            fields=['name', 'description', 'status', 'executor']
            )
        task_dict['name'] = 'failllllllzzz'
        response = self.client.post(update_url, task_dict)
        self.assertEqual(response.status_code, 302)
 
        response = self.client.get(self.task_list_url)
        self.assertTrue(Task.objects.filter(name='failllllllzzz').exists())
        self.assertContains(response, 'failllllllzzz')
        self.assertNotContains(response, '[p[p[p[ppp')  # previous value

    def test_task_delete(self):
        delete_url = reverse('task_delete', kwargs={'pk': self.test_task.pk})

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.task_list_url)
        self.assertNotContains(response, 'asdasdzzzzzzz')


    
