from django.db import models
from django.contrib.auth.models import User
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

# Create your models here.

# class UserProfileInfoForm(models.Model):    
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     portfolio_site = models.URLField(blank=True)
#     profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
#     def __str__(self):
#         return self.user.username

class NewAccount(models.Model):
    def __str__(self):
        return 'Account added: {}'.format(self.Username)

    Username = models.CharField(max_length=25)
    First_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=25)
    Category = models.CharField(max_length=25)
    # Category choices begin here
    ADMIN = 'Admin'
    MANAGER = 'Manager'
    EMPLOYEE = 'Employee'
    STAFF = 'Staff'
    CATEGORY_CHOICES = [
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee'),
        (STAFF, 'Staff'),        
    ]
    Category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=ADMIN,
    )
    # Category choices end here

    Status = models.CharField(max_length=25)
    # Status choices begin here
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'        
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),               
    ]
    Status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )
    # Status choices end here

    Experience = models.CharField(max_length=40)
    # Experience choices begin here
    FRESHER = 'Fresher'
    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    EXPERIENCE_CHOICES = [
        (FRESHER, 'Fresher'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),        
    ]
    Experience = models.CharField(
        max_length=10,
        choices=EXPERIENCE_CHOICES,
        default=FRESHER,
    )
    # Experience choices end here

    Performance = models.CharField(max_length=25)
    # Performance choices begin here
    BAD = 'Bad'
    AVERAGE = 'Average'
    GOOD = 'Good'
    EXCELLENT = 'Excellent'    
    PERFORMANCE_CHOICES = [
        (BAD, 'Bad'),
        (AVERAGE, 'Average'),
        (GOOD, 'Good'),
        (EXCELLENT, 'Excellent'),        
    ]
    Performance = models.CharField(
        max_length=10,
        choices=PERFORMANCE_CHOICES,
        default=AVERAGE,
    )
    # Performance choices end here

    # Define DB table name here
    class meta:
        db_table = "dappx_newaccount"
    
# class AddAccount(models.Model):
#     Username = models.CharField(max_length=25)
#     First_Name = models.CharField(max_length=25)
#     Last_Name = models.CharField(max_length=25)
#     Category = models.CharField(max_length=25)
#     Status = models.CharField(max_length=25)
#     Experience = models.CharField(max_length=25)
#     Performance = models.CharField(max_length=25)
#     class meta:
#         db_table = "dappx_addaccount"