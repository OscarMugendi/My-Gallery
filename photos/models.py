from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length =80)


    @classmethod
    def get_locations(cls):
        locations = cls.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)       
    
    def save_location(self):
        self.save()    
    
    def delete_location(self):
        self.delete()


    class Meta:
        ordering = ["name"]
        verbose_name = "Location"
        verbose_name_plural = "Locations" 
    

class Category(models.Model):
    name = models.CharField(max_length =80)

    def __str__(self):
        return self.name 
    
    def save_category(self):
            self.save()
    
    def delete_category(self):
        self.delete()


    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        

class Image(models.Model):
    name = models.CharField(max_length =80)
    description = models.TextField()
    location = models.ForeignKey(Location, related_name='location', on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.DO_NOTHING)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to = 'images/')

    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.description[:100]+" ......"

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()    


    class Meta:
        ordering = ["pub_date"]
        verbose_name = "Image"
        verbose_name_plural = "Images" 