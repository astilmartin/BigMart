from django.db import models

# Create your models here.
class categorydb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=500,null=True,blank=True)
    Image=models.ImageField(upload_to="Product Images",null=True,blank=True)


class productdb(models.Model):
    Category=models.CharField(max_length=100,null=True,blank=True)
    Product_Name=models.CharField(max_length=100,null=True,blank=True)
    Product_price = models.IntegerField(null=True, blank=True)
    P_Description=models.CharField(max_length=500,null=True,blank=True)
    Product_Image=models.ImageField(upload_to="Product Main Images",null=True,blank=True)