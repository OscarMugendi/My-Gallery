from django.test import TestCase

from .models import Image, Category, Location


class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='test_location')
        self.location.save_location()

        self.category = Category(name='test_category')
        self.category.save_category()

        self.image_test = Image(id=1, name='test_image', description='this is a test description', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='test_location')
        self.assertTrue(len(found_images) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='test_location')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='test_category')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)