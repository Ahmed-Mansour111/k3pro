from django.db import models
from rep.models import Rep
from datetime import datetime

# Create your models here.
class Listing(models.Model):

    USB_TYPE=(
            ('V8','V8'),
            ('IP','IPHONE'),
            ('TYPE-C','TYPE-C'),
            ('3.5','3.5')
    )


    rep=models.ForeignKey( Rep , on_delete=models.DO_NOTHING )
    product =models.CharField(max_length=200)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL , null=True)
    model = models.CharField(max_length=20)
    USB_Type = models.CharField(max_length=100 , choices=USB_TYPE , default='V8')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/')
    photo_1=models.ImageField(upload_to='photos/',blank=True)
    photo_2=models.ImageField(upload_to='photos/',blank=True)
    photo_3=models.ImageField(upload_to='photos/',blank=True)
    photo_4=models.ImageField(upload_to='photos/',blank=True)
    photo_5=models.ImageField(upload_to='photos/',blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.product


class Category(models.Model):
    category_name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='photos/category/', blank=True , null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name



class HomeImage(models.Model):
    image_name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='photos/home-image/', blank=True , null=True)

    def __str__(self):
        return self.image_name
