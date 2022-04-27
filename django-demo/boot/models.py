from django.db import models
from django.forms import CharField, EmailField, IntegerField

# Create your models here.

class Inquiry(models.Model):
        fullname = models.CharField(max_length=64,  blank=True)
        emailaddress =  models.CharField(max_length=64, blank=True)
        phonenum = models.CharField(max_length=64, blank=True)
        message =  models.TextField (blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)

