
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
    myImage = CloudinaryField('image')
    vacancy = models.IntegerField(default=7)

    def __str__(self):
        return self.name


class Team(models.Model):
    teamID = models.CharField(max_length=100, default='CSE')
    project_name = models.CharField(max_length=100)
    project_domain = models.CharField(max_length=100)
    project_description = models.TextField(blank=True, null=True,)
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

    reg_no_3 = models.BigIntegerField(blank=True, null=True)
    student_3_name = models.CharField(max_length=100, blank=True, null=True)
    student_3_email = models.CharField(max_length=100, blank=True, null=True)
    student_3_no = models.BigIntegerField(blank=True, null=True)

    guide = models.CharField(
        max_length=100)

    guide_email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.project_name + ' ' + self.student_1_name + ' Added Sucessfully.'


class Temp_Team(models.Model):
    teamID = models.CharField(max_length=100, default='CSE')
    project_name = models.CharField(max_length=100)
    project_domain = models.CharField(max_length=100)
    project_description = models.TextField(blank=True, null=True)
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

    reg_no_3 = models.BigIntegerField(blank=True, null=True)
    student_3_name = models.CharField(max_length=100, blank=True, null=True)
    student_3_email = models.CharField(max_length=100, blank=True, null=True)
    student_3_no = models.BigIntegerField(blank=True, null=True)
    guide = models.CharField(
        max_length=100, null=True)

    guide_email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.project_name + ' ' + self.student_1_name + ' Added Sucessfully.'


class Otp(models.Model):
    user_email = models.CharField(max_length=100)
    otp = models.CharField(max_length=10)

    def __str__(self):
        return self.user_email


class Otp_Two(models.Model):
    user_email = models.CharField(max_length=100)
    temp_email = models.CharField(max_length=100, blank=True, null=True)
    otp = models.CharField(max_length=10)

    def __str__(self):
        return self.user_email


class Temp_User(models.Model):
    user_email = models.EmailField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user_email
