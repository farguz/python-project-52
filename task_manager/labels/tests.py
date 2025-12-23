from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Label


class LabelsTest(TestCase):

    fixtures = [
        'labels.json',
        'users.json']
    
    def setUp(self): 
        self.label_list_url = reverse('label_list')

        self.User = get_user_model()
        self.admin_user = self.User.objects.get(pk=1)
        self.client.force_login(self.admin_user) 

        self.test_label = Label.objects.get(pk=2)

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
        update_url = reverse('label_update', kwargs={'pk': self.test_label.pk})

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        label_to_update = {key: value for key, value in self.test_label.__dict__.items() if value}
        updated_label = {**label_to_update, 'name': 'sexy_love_t-ara'}
        response = self.client.post(update_url, updated_label)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.label_list_url)
        self.assertContains(response, 'sexy_love_t-ara')
        self.assertNotContains(response, 'adggda; fixed')  # 'adggda; fixed' - previous value

    def test_label_delete(self):
        delete_url = reverse('label_delete', kwargs={'pk': self.test_label.pk})

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.label_list_url)
        self.assertNotContains(response, 'adggda; fixed')


    
