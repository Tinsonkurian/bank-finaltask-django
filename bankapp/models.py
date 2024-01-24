from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class District(models.Model):
    dist_name = models.CharField(max_length=250)

    def __str__(self):
        return self.dist_name

class Branches(models.Model):
    branch_name = models.CharField( max_length=250)
    district_name = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.branch_name
    
class AccountType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Materials(models.Model):
    items = models.CharField( max_length=250)

    def __str__(self):
        return self.items

class Userdetails(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE, null=True)
    materials = models.CharField( max_length=250, null=True)
    materials_provide = models.CharField(max_length=255, null=True, blank=True, default='1: debit card, 2: credit card, 3: cheque book')  # Allow null values
    
    def __str__(self):
        return self.name