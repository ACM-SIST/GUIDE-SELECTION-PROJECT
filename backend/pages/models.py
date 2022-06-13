

from .choices import no_members_choices
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Guide(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField(default=1)
    serial_no = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    domain_1 = models.CharField(max_length=200)
    domain_2 = models.CharField(max_length=200, blank=True)
    domain_3 = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200)
    experience = models.IntegerField()
    # myImage = models.ImageField(upload_to='photos/%Y/%m/%d')
    myImage = CloudinaryField('image')
    vacancy = models.IntegerField(default=7)

    def __str__(self):
        return self.name


class Team(models.Model):
    teamID = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    project_domain = models.CharField(max_length=100)
    project_description = models.TextField()
    no_of_members = models.CharField(
        max_length=10, choices=no_members_choices, default='1')

    reg_no_1 = models.BigIntegerField()

    student_1_name = models.CharField(max_length=100)

    student_1_email = models.CharField(max_length=100)

    student_1_no = models.BigIntegerField()

    reg_no_2 = models.BigIntegerField(blank=True, null=True)

    student_2_name = models.CharField(max_length=100, blank=True, null=True)

    student_2_email = models.CharField(max_length=100, blank=True, null=True)

    student_2_no = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.project_name + ' ' + self.student_1_name + ' Added Sucessfully.'
