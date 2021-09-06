from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length =80, unique='True')
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Location"
        verbose_name_plural = "Locations"        
    
    def save_location(self):
        self.save()    
    
    def delete_location(self):
        self.delete()

    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length =80, unique='True')
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def save_category(self):
            self.save()
    
    def delete_category(self):
        self.delete()

    @classmethod
    def get_category(cls):
        categories = cls.objects.all()
        return categories

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__category__icontains=search_term)
        return images

    def __str__(self):
        return self.name  
        

class Image(models.Model):
    name = models.CharField(max_length =80)
    description = models.TextField()
    location = models.ForeignKey(Location, related_name='location', on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.DO_NOTHING)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to = 'images/')
    
    class Meta:
        ordering = ["pub_date"]
        verbose_name = "Image"
        verbose_name_plural = "Images" 
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.description[:100]+" ......"
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()    

    def get_image_by_id(cls):
        images = cls.objects.get(pk=id)
        return images

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
    
    def search_image(category):
        pass
    
    def filter_by_location(location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location
    
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def search_by_category(cls,search_term):
        searched_images = cls.objects.filter(category__category__icontains=search_term)
        return searched_images

    @classmethod
    def search_by_location(cls, location):
        images = cls.objects.filter(location__location=location)
        return images

    @classmethod
    def get_by_category(cls, category):
        images = cls.objects.filter(category__category=category)
        return images

    @classmethod
    def get_image(request, id):
        locations = Location.get_location()
        try:
            image = Image.objects.get(pk = id)
            print(image)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return image
    
    def __str__(self):
        return self.name