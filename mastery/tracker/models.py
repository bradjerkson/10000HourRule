from django.db import models

# Create your models here.
#https://www.javatpoint.com/django-crud-application
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
class Meta:
    db_table= "user"
