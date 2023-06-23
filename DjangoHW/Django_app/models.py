from django.db import models


# Create your models here.

class Informations(models.Model):
    First_name = models.CharField(max_length=12, null=False)
    Last_name = models.CharField(max_length=12, null=False)
    Email = models.EmailField(max_length=40, null=False)
    Phone_number = models.CharField(max_length=12, null=False)
    Address1 = models.CharField(max_length=102, null=False)
    Product_id = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f'first name:{self.First_name} Last name: {self.Last_name}'


