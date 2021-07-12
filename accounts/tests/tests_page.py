from django.test import TestCase
from django.urls import reverse


class PageTestCase(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_mentions_legales_page(self):
        response = self.client.get(reverse('ml'))
        self.assertEqual(response.status_code, 200)

    def test_my_account_page(self):
        response = self.client.get(reverse('my_account'))
        self.assertEqual(response.status_code, 302)
