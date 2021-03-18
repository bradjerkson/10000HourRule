from django.db import models
#import JSONField

# Create your models here.
#https://www.javatpoint.com/django-crud-application
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

class Skill_List(models.Model):
    skill_username = models.ForeignKey(User, on_delete=models.CASCADE)


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_hours = models.DecimalField(max_digits=7, decimal_places=2)
    #skill_tags = models.JSONField()
    #skill_attributes = models.JSONField()
    skill_list = models.ForeignKey(Skill_List, on_delete=models.CASCADE)




"""
class Meta:
    db_table= "user"
"""
