from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_user = models.BooleanField(default=False)




class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='customer')
    Name = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField()