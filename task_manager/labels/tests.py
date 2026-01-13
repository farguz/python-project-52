from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Label


class LabelsTest(TestCase):
    '''
    any auth user can modify any label
    any user can delete label except label linked with task
    '''

    fixtures = [
        'statuses.json',
        'users.json',
        'tasks.json',
        'labels.json',
        ]
    
    def setUp(self): 
        self.label_list_url = reverse('label_list')

        self.User = get_user_model()
        self.random_user = self.User.objects.get(pk=11)
        self.client.force_login(self.random_user) 

        self.test_label_linked = Label.objects.get(pk=2)
        self.test_label_non_linked = Label.objects.get(pk=10)

    def test_label_list(self):
        response = self.client.get(self.label_list_url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('labels', response.context)

        labels = response.context['labels']
        self.assertTrue(len(labels) > 0)

    def test_label_create(self):
        create_url = reverse('label_create')

        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)

        new_label = {
            'name': 'boombayah',
            }
        response = self.client.post(create_url, new_label)
        self.assertEqual(response.status_code, 302)  # 302 redirect

        response = self.client.get(self.label_list_url)
        self.assertContains(response, 'boombayah')  # html
        self.assertTrue(Label.objects.filter(name='boombayah').exists())  # database

    def test_label_update(self):
        update_url = reverse('label_update', kwargs={'pk': self.test_label_linked.pk})

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        updated_label = {'name': 'sexy_love_t-ara'}
        response = self.client.post(update_url, updated_label)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.label_list_url)
        # 'sexy_love_t-ara' - new value
        self.assertContains(response, 'sexy_love_t-ara')
        # 'adggda; fixed' - previous value
        self.assertNotContains(response, 'adggda; fixed')  

    def test_label_delete(self):
        delete_url = reverse('label_delete', kwargs={'pk': self.test_label_non_linked.pk})

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.label_list_url)
        self.assertNotContains(response, 'fsjogij4tug49jrvij')
        self.assertFalse(Label.objects.filter(name='fsjogij4tug49jrvij').exists())

    def test_label_linked_delete(self):
        delete_url = reverse('label_delete', kwargs={'pk': self.test_label_linked.pk})

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.label_list_url)
        self.assertContains(response, 'cannot be deleted')
        self.assertContains(response, 'adggda; fixed')
        self.assertTrue(Label.objects.filter(name='adggda; fixed').exists())
