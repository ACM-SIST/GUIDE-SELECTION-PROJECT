
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Guide(models.Model):
    name = models.CharField(max_length=100)
    domain_1 = models.CharField(max_length=20)
    domain_2 = models.CharField(max_length=20)
    domain_3 = models.CharField(max_length=20)
    email = models.CharField(max_length=29)
    experience = models.IntegerField()
    # myImage = models.ImageField(upload_to='photos/%Y/%m/%d')
    myImage = CloudinaryField('image')
    vacancy = models.IntegerField(default=7)

    def __str__(self):
        return self.name
