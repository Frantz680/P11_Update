from django.test import TestCase
from django.urls import reverse

from purbeurre.models import Category_product, Name


class DataTests(TestCase):

    def setUp(self):
        fruits = Category_product.objects.create(name_category='fruits')

        Name.objects.create(name_product='pomme',
                            category=fruits,
                            nutrition_grade='a',
                            picture_product='www.pomme.com',
                            picture_nutrition='www.pomme_nutri_grade.com',
                            url_product='www.openfoodfact_pomme.com')

    def test_search_200(self):
        pomme = str('pomme')
        response = self.client.get(reverse('search'), {
            'search_user': pomme,
        })
        self.assertEqual(response.status_code, 302)

    def test_search_302(self):
        pomme = str('pomme_pas_bon')
        response = self.client.get(reverse('search'), {
            'search_user': pomme,
        })
        self.assertEqual(response.status_code, 302)

    def test_my_account_302(self):
        pomme = str('pomme')
        response = self.client.get(reverse('my_account'), {
            'my_product': pomme,
        })
        self.assertEqual(response.status_code, 302)
