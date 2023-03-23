from django.db import models

# Create your models here.


class Book1(models.Model):
   id=models.AutoField(primary_key=True)
   title=models.CharField(max_length=32)
   pub_data=models.DateField()
   price=models.DecimalField(max_digits=8,decimal_places=2)
   publish=models.CharField(max_length=32)


   def __str__(self):
       return '%s,%s'%(self.title,self.price)

class Author(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    age=models.IntegerField()

    #一对一
    authordetail=models.OneToOneField(to="AuthorDetail",to_field="nid",on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    nid=models.AutoField(primary_key=True)
    birthday=models.DateField()
    telephone=models.BigIntegerField()
    addr=models.CharField(max_length=64)



#出版社
class Publish(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    city=models.CharField(max_length=32)
    email=models.EmailField()


class Book(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    #一对多
    publish=models.ForeignKey(to="Publish",to_field="nid",on_delete=models.CASCADE)

    #多对多
    authors=models.ManyToManyField(to="Author")