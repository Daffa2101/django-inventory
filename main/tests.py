from django.test import TestCase, Client
from .models import Item


class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    # Periksa tipe data kolom 'name'

    def test_name_field_type(self):
        item = Item(name="test item", amount=1,
                    description="test", category="test")

        self.assertIs(type(item.name), str)

    # Periksa tipe data kolom 'amount'

    def test_amount_field_type(self):
        item = Item(name="test item", amount=1,
                    description="test", category="test")
        self.assertIs(type(item.amount), int)

    # Periksa tipe data kolom 'description'

    def test_description_field_type(self):
        item = Item(name="test item", amount=1,
                    description="test", category="test")
        self.assertIs(type(item.description), str)

    # Periksa tipe data kolom 'category'

    def test_category_field_type(self):
        item = Item(name="test item", amount=1,
                    description="test", category="test")
        self.assertIs(type(item.category), str)
