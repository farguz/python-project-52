from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

from .models import Task
from .views import IndexTaskView


class TasksTest(TestCase):
    '''
    any user can modify any task
    only task creator or admin can delete task
    '''
    
    fixtures = [
        'tasks.json',
        'users.json',
        'statuses.json',
        'labels.json',
        ]
    
    def setUp(self): 
        self.task_list_url = reverse('task_list')

        self.User = get_user_model()
        self.test_user_creator = self.User.objects.get(pk=22)  # oopoipoipkkpo
        self.test_user_not_creator = self.User.objects.get(pk=23)  # kdakldak
        self.client.force_login(self.test_user_creator)

        self.test_task = Task.objects.get(pk=32)  # afaadsafloteff
        self.all_tasks = Task.objects.all()

        self.test_label = Label.objects.get(pk=5)  # popopozzze
        self.test_status = Status.objects.get(pk=9)  # asdasdaaaqqq

    def test_task_list(self):
        response = self.client.get(self.task_list_url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('tasks', response.context)

        tasks = response.context['tasks']
        self.assertTrue(len(tasks) > 0)
        self.assertTrue(len(tasks) < 11)  # pagination check

    @patch.object(IndexTaskView, 'paginate_by', 9999)
    def test_task_create(self):
        create_url = reverse('task_create')

        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)

        new_task = {
            "name": "ppokpokpok",
            "description": "opkooiopsaads",
            "status": 9,
            "creator": 1,
            "executor": 11,
            "labels": [4, ],
            }
        response = self.client.post(create_url, new_task)
        self.assertEqual(response.status_code, 302)  # 302 redirect

        response = self.client.get(self.task_list_url)
        self.assertContains(response, 'ppokpokpok')  # html
        self.assertTrue(Task.objects.filter(name='ppokpokpok').exists())  # database

    @patch.object(IndexTaskView, 'paginate_by', 9999)
    def test_task_update(self):
        update_url = reverse('task_update', kwargs={'pk': self.test_task.pk})

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        task_dict = model_to_dict(
            self.test_task,
            fields=['name', 'description', 'status', 'executor', 'labels', ]
            )
        task_dict['name'] = 'failllllllzzz'
        task_dict['labels'] = [label.pk for label in self.test_task.labels.all()]
        response = self.client.post(update_url, task_dict)
        self.assertEqual(response.status_code, 302)
 
        response = self.client.get(self.task_list_url)
        self.assertTrue(Task.objects.filter(name='failllllllzzz').exists())
        self.assertContains(response, 'failllllllzzz')
        self.assertNotContains(response, 'afaadsafloteff')  # previous value
        self.assertTrue(Task.objects.filter(name='failllllllzzz').exists())
        self.assertFalse(Task.objects.filter(name='afaadsafloteff').exists())

    @patch.object(IndexTaskView, 'paginate_by', 9999)
    def test_task_delete_by_creator(self):
        delete_url = reverse('task_delete', kwargs={'pk': self.test_task.pk})

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.task_list_url)
        self.assertNotContains(response, 'afaadsafloteff')  
        self.assertFalse(Task.objects.filter(name='afaadsafloteff').exists())  

    @patch.object(IndexTaskView, 'paginate_by', 9999)
    def test_task_delete_by_not_creator(self):
        delete_url = reverse('task_delete', kwargs={'pk': self.test_task.pk})

        self.client.force_login(self.test_user_not_creator)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.task_list_url)
        self.assertContains(response, 'afaadsafloteff') 
        self.assertTrue(Task.objects.filter(name='afaadsafloteff').exists())

    def test_task_filter_executor(self):
        filter_data = {'executor': self.test_user_not_creator.pk}

        response = self.client.get(self.task_list_url, filter_data)
        self.assertEqual(response.status_code, 200)

        tasks = response.context['tasks']
        self.assertTrue(len(tasks) == 1)

    def test_task_filter_status(self):
        filter_data = {'status': self.test_status.pk}

        response = self.client.get(self.task_list_url, filter_data)
        self.assertEqual(response.status_code, 200)

        tasks = response.context['tasks']
        self.assertTrue(len(tasks) == 3)

    def test_task_filter_label(self):
        filter_data = {'labels': self.test_label.pk}

        response = self.client.get(self.task_list_url, filter_data)
        self.assertEqual(response.status_code, 200)

        tasks = response.context['tasks']
        self.assertTrue(len(tasks) == 4)

    def test_task_filter_im_creator(self):
        filter_data = {'creator': self.test_user_creator.pk}

        response = self.client.get(self.task_list_url, filter_data)
        self.assertEqual(response.status_code, 200)

        tasks = response.context['tasks']
        self.assertTrue(len(tasks) == 7)

    def test_task_filter_im_executor(self):
        filter_data = {'executor': self.test_user_creator.pk}

        response = self.client.get(self.task_list_url, filter_data)
        self.assertEqual(response.status_code, 200)

        tasks = response.context['tasks']
        self.assertTrue(len(tasks) == 3)
