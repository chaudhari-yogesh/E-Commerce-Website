from distutils.command.upload import upload
from email.policy import default
from itertools import product
from pyexpat import model
from unittest.util import _MAX_LENGTH
from xml.sax.handler import all_properties
from django.db import models

# Create your models here.

class Product(models.Model):
   
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    category= models.CharField(max_length=50, default="")
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    sub_category=models.CharField(max_length=50, default="")
    Images= models.ImageField(upload_to= "shop/images", default="")


    def __str__(self):
        return self.product_name


class Contact(models.Model):
    name= models.CharField(max_length=30);
    gmail= models.CharField(max_length=30);
    phonenumber= models.IntegerField(max_length=12);
    address= models.CharField(max_length=50);
    txtarea= models.TextField();

    def __str__(self) -> str:
        return self.name

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True);
    items_json = models.CharField(max_length=5000, default="");
    name= models.CharField(max_length=30);
    gmail= models.CharField(max_length=30);
    amount= models.IntegerField(default=0)
    mobilenumber= models.CharField(max_length=12, default="");
    address= models.CharField(max_length=50);
    city= models.CharField(max_length=10);
    state= models.CharField(max_length=10);
    zip_code= models.CharField(max_length=10 ,default="");
    
class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."