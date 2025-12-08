from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from statuses.models import Status

# Create your tests here.


class StatusesTest(TestCase):

    fixtures = [
        'statuses.json',
        '../../users/fixtures/users.json']
    
    def setUp(self): 
        self.status_list_url = reverse('status_list')

        self.User = get_user_model()
        self.admin_user = self.User.objects.get(pk=1)
        self.client.force_login(self.admin_user) 

        self.test_status = Status.objects.get(pk=9)

    def test_status_list(self):
        response = self.client.get(self.status_list_url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('statuses', response.context)

        statuses = response.context['statuses']
        self.assertTrue(len(statuses) > 0)

    def test_status_create(self):
        create_url = reverse('status_create')

        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)

        new_status = {
            'name': 'in progresssss',
            }
        response = self.client.post(create_url, new_status)
        self.assertEqual(response.status_code, 302)  # 302 redirect

        response = self.client.get(self.status_list_url)
        self.assertContains(response, 'in progresssss')  # html
        self.assertTrue(Status.objects.filter(name='in progresssss').exists())  # database

    def test_status_update(self):
        update_url = reverse('status_update', kwargs={'id': self.test_status.pk})

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        status_to_update = {key: value for key, value in self.test_status.__dict__.items() if value}
        updated_status = {**status_to_update, 'name': 'failllllll'}
        response = self.client.post(update_url, updated_status)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.status_list_url)
        self.assertContains(response, 'failllllll')
        self.assertNotContains(response, 'asdasdzzzzzzz')  # asdasdzzzzzzz - previous value

    def test_status_delete(self):
        delete_url = reverse('status_delete', kwargs={'id': self.test_status.pk})

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.status_list_url)
        self.assertNotContains(response, 'asdasdzzzzzzz')


    
