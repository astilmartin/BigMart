from django.db import models

# Create your models here.

class contactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=500,null=True,blank=True)

class registerdb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)


class cartdb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    ProductName = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)