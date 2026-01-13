from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Status

# Create your tests here.


class StatusesTest(TestCase):
    '''
    any auth user can modify any status
    any user can delete status except status linked with task
    '''

    fixtures = [
        'statuses.json',
        'users.json',
        'tasks.json',
        'labels.json',
        ]
    
    def setUp(self): 
        self.status_list_url = reverse('status_list')

        self.User = get_user_model()
        self.random_user = self.User.objects.get(pk=11)
        self.client.force_login(self.random_user) 
        
        self.test_status_linked = Status.objects.get(pk=10)
        self.test_status_non_linked = Status.objects.get(pk=22)

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
        # 302 redirect
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.status_list_url)
        # html
        self.assertContains(response, 'in progresssss')  
        # database
        self.assertTrue(
            Status.objects.filter(name='in progresssss').exists()
            )  

    def test_status_update(self):
        update_url = reverse(
            'status_update',
            kwargs={'pk': self.test_status_linked.pk}
            )

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        updated_status = {'name': 'failllllll'}
        response = self.client.post(update_url, updated_status)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.status_list_url)
        self.assertContains(response, 'failllllll')
        # aaaaaaqqqqqqqqqqqqrrrr - previous value
        self.assertNotContains(response, 'aaaaaaqqqqqqqqqqqqrrrr') 

    def test_status_delete(self):
        delete_url = reverse('status_delete', kwargs={'pk': self.test_status_non_linked.pk})

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.status_list_url)
        self.assertNotContains(response, 'kfwrpogjrp3rewfdsk')
        self.assertFalse(
            Status.objects.filter(name='kfwrpogjrp3rewfdsk').exists()
            )  

    def test_status_linked_delete(self):
        delete_url = reverse('status_delete', kwargs={'pk': self.test_status_linked.pk})
        
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.status_list_url)
        self.assertContains(response, 'cannot be deleted')
        self.assertContains(response, 'aaaaaaqqqqqqqqqqqqrrrr')
        self.assertTrue(
            Status.objects.filter(name='aaaaaaqqqqqqqqqqqqrrrr').exists()
            )
