from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    name=models.TextField()
    dis=models.TextField()
    img=models.FileField()
    

class Contact(models.Model):
    name=models.TextField()
    email=models.EmailField()
    message=models.TextField()
    phone=models.IntegerField()
    subject=models.TextField()