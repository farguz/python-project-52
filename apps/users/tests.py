from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class UsersTest(TestCase):

    fixtures = ['users.json']
    
    def setUp(self): 
        self.user_list_url = reverse('user_list')
        self.User = get_user_model()
        self.test_user = self.User.objects.get(pk=12)

        self.admin_user = self.User.objects.get(pk=1)
        self.client.force_login(self.admin_user) 

    def test_user_list(self):
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('users', response.context)

        users = response.context['users']
        self.assertTrue(len(users) > 0)

    def test_user_create(self):
        create_url = reverse('user_create')

        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)

        new_user = {
            'first_name': 'Kate',
            'last_name': 'Pepper',
            'username': 'kitty_meow_90',
            'password1': 'sadsadasd12',
            'password2': 'sadsadasd12',
            }
        response = self.client.post(create_url, new_user)
        self.assertEqual(response.status_code, 302)  # 302: redirect login page

        response = self.client.get(self.user_list_url)
        self.assertContains(response, 'kitty_meow_90')  # html
        self.assertTrue(self.User.objects.filter(username='kitty_meow_90').exists())  # database

    def test_user_update(self):
        update_url = reverse('user_update', kwargs={'id': self.test_user.pk})

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        user_to_update = {key: value for key, value in self.test_user.__dict__.items() if value}
        updated_user = {**user_to_update, 'first_name': 'Bobbbbzzy'}
        response = self.client.post(update_url, updated_user)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.user_list_url)
        self.assertContains(response, 'Bobbbbzzy')
        self.assertNotContains(response, 'janettttty')  # previous first_name

    def test_user_delete(self):
        delete_url = reverse('user_delete', kwargs={'id': self.test_user.pk})

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.user_list_url)
        self.assertNotContains(response, 'janettttty')


    
