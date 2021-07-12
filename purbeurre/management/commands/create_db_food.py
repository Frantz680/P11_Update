import requests

from django.core.management.base import BaseCommand
from django.db.utils import DataError, IntegrityError
from purbeurre.models import Category_product, Name


class Command(BaseCommand):
    """
    This
    class is used for information retrieval in the API.
    """

    CATEGORIES = ['Biscuits', 'Boissons-gazeuses', 'Chocolats',
                  'Epicerie', 'Fromages-de-france', 'Glace',
                  'Poissons', 'Pates-a-tartiner', 'Pains',
                  'Pizzas', 'Snacks sucrés', 'Viandes', 'Vins',
                  'Yaourts']

    def request_category(self):

        for category in self.CATEGORIES:
            name_category = Category_product.objects.create(
                name_category=category)

            params = {
                    'action': 'process',
                    'json': 1,
                    'page_size': 500,
                    'page': 1,
                    'tagtype_0': 'categories',
                    'tag_contains_0': 'contains',
                    'tag_0': category,
                }

            response = requests.get(
                'https://fr.openfoodfacts.org/cgi/search.pl',
                params=params)

            data = response.json()
            products = data['products']

            for product in products:
                try:
                    name_product = product["product_name"]
                    nutrition_grade = product["nutrition_grades"]
                    picture_product = product['image_front_url']
                    picture_nutrition = product["image_nutrition_small_url"]
                    url_product = product["url"]

                    Name.objects.create(name_product=name_product,
                                        category=name_category,
                                        nutrition_grade=nutrition_grade,
                                        url_product=url_product,
                                        picture_product=picture_product,
                                        picture_nutrition=picture_nutrition)

                except KeyError:
                    pass

                except DataError:
                    pass

                except IntegrityError:
                    pass

    def handle(self, *args, **options):
        self.request_category()
