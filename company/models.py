from django.db import models
from users.models import User

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100,default='none')
    tin = models.PositiveBigIntegerField(default=0)
    licence = models.FileField(upload_to='licence', null=True, blank=True)

    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Startup(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    address = models.CharField(max_length=200)
    phonenumber = models.PositiveBigIntegerField()
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name