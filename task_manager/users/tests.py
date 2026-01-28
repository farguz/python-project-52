from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .views import IndexUserView


class UsersTest(TestCase):
    '''
    only profile owner or admin able to upd/del account
    user list page are available for everyone
    '''

    fixtures = ['users.json']
    
    def setUp(self):
        self.user_list_url = reverse('user_list')

        self.User = get_user_model()
        self.test_user = self.User.objects.get(pk=16)
        self.non_admin_user = self.User.objects.get(pk=13)
        self.admin_user = self.User.objects.get(pk=1)

        self.updated_user = {
            'first_name': 'Bobbbbzzy',
            'last_name': self.test_user.last_name,
            'username': self.test_user.username,
            }
        
        self.new_user = {
            'first_name': 'Kate',
            'last_name': 'Pepper',
            'username': 'kitty_meow_90',
            'password1': 'sadsadasd12',
            'password2': 'sadsadasd12',
            }
        
    def test_user_list(self):
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('users', response.context)

        users = response.context['users']
        self.assertTrue(len(users) > 0)
        self.assertTrue(len(users) < 11)  # pagination check

    @patch.object(IndexUserView, 'paginate_by', 9999)
    def test_user_create(self):
        create_url = reverse('user_create')

        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(create_url, self.new_user)

        # 302: redirect login page
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.user_list_url)

        # html
        self.assertContains(response, 'kitty_meow_90')

        # database
        self.assertTrue(
            self.User.objects.filter(username='kitty_meow_90').exists()
            )

    @patch.object(IndexUserView, 'paginate_by', 9999)
    def test_user_update_by_admin(self):
        update_url = reverse(
            'user_update',
            kwargs={'pk': self.test_user.pk}
        )

        self.client.force_login(self.admin_user) 

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(update_url, self.updated_user)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.user_list_url)
        # Bobbbbzzy is new first_name
        self.assertContains(response, 'Bobbbbzzy')
        # lljroeiuo is previous first_name
        self.assertNotContains(response, 'lljroeiuo')
        self.assertTrue(
            self.User.objects.filter(first_name='Bobbbbzzy').exists()
            )
        self.assertFalse(
            self.User.objects.filter(first_name='lljroeiuo').exists()
            )

    @patch.object(IndexUserView, 'paginate_by', 9999)
    def test_user_update_by_non_admin(self):
        update_url = reverse(
            'user_update',
            kwargs={'pk': self.test_user.pk}
        )

        self.client.force_login(self.non_admin_user) 
        response = self.client.post(update_url, self.updated_user)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.user_list_url)
        # flash 'Forbidden. Not enough rights...
        self.assertContains(response, 'Forbidden')
        self.assertContains(response, 'lljroeiuo')
        
        self.client.force_login(self.test_user)
        response = self.client.post(update_url, self.updated_user)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.user_list_url)
        # Bobbbbzzy is new first_name
        self.assertContains(response, 'Bobbbbzzy')
        # janettttty is previous first_name
        self.assertNotContains(response, 'lljroeiuo')
        self.assertTrue(
            self.User.objects.filter(first_name='Bobbbbzzy').exists()
            )
        self.assertFalse(
            self.User.objects.filter(first_name='lljroeiuo').exists()
            )

    @patch.object(IndexUserView, 'paginate_by', 9999)
    def test_user_delete_by_admin(self):
        delete_url = reverse(
            'user_delete',
            kwargs={'pk': self.test_user.pk}
        )

        self.client.force_login(self.admin_user) 
        
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.user_list_url)
        self.assertNotContains(response, 'lljroeiuo')
        self.assertFalse(
            self.User.objects.filter(first_name='lljroeiuo').exists()
            )

    @patch.object(IndexUserView, 'paginate_by', 9999)
    def test_user_delete_by_non_admin(self):
        delete_url = reverse(
            'user_delete',
            kwargs={'pk': self.test_user.pk}
        )

        self.client.force_login(self.non_admin_user) 
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.user_list_url)
        # flash 'Forbidden. Not enough rights...'
        self.assertContains(response, 'Forbidden')
        # user still there, 'lljroeiuo' is first name
        self.assertContains(response, 'lljroeiuo')

        self.client.force_login(self.test_user) 
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.user_list_url)
        self.assertNotContains(response, 'lljroeiuo')
        self.assertFalse(
            self.User.objects.filter(first_name='lljroeiuo').exists()
            )
