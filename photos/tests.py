from django.test import TestCase
from .models import Image, Location, Category
import datetime as dt

# Create your tests here.

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.loc1= Location(name = 'Nairobi')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.loc1,Location))


class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat1 = Category(name = 'Wild')


class ImageTestClass(TestCase):
    def setUp(self):
        self.image1= Location(name = 'Nairobi')
        self.image1.save_location()
        
        self.new_image= Image(name = 'CBD',description = 'This is a random description',location = self.image1)
        self.new_image.save()