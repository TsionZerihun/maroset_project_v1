from django.db import models
from users.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    tin = models.PositiveBigIntegerField(null=True, blank=True)
    trade_licence = models.PositiveBigIntegerField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name