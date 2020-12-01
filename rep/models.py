from django.db import models

# Create your models here.
class Rep(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100 , default='Employee')
    photo = models.ImageField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp= models.BooleanField(default=False)

    def __str__(self):
        return self.name