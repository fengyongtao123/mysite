from django.db import models

# Create your models here.


class Book_stu(models.Model):
   id=models.AutoField(primary_key=True)
   title=models.CharField(max_length=32)
   pub_data=models.DateField()
   price=models.DecimalField(max_digits=8,decimal_places=2)
   publish=models.CharField(max_length=32)

   def __str__(self):
       return "%s,%s"%(self.title,self.price)


class User(models.Model):
    name=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)


class Shu(models.Model):
    title=models.CharField(max_length=32)
    price=models.DecimalField(decimal_places=2,max_digits=8)