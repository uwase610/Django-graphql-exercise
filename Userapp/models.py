from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phoneno = models.IntegerField()


    def __str__(self):
        return self.name
