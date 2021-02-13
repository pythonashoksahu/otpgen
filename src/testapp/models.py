from django.db import models

# Create your models here.
class Otp(models.Model):
    account=Models.FloatField()


    def __str__(self):
        return str(self.account)

