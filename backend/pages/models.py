

from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Guide(models.Model):
    name = models.CharField(max_length=100)
    domain_1 = models.CharField(max_length=200)
    domain_2 = models.CharField(max_length=200)
    domain_3 = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    experience = models.IntegerField()
    # myImage = models.ImageField(upload_to='photos/%Y/%m/%d')
    myImage = CloudinaryField('image')
    vacancy = models.IntegerField(default=7)

    def __str__(self):
        return self.name
