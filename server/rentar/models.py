from django.db import models

class Apartment(models.Model):
	address_text = models.CharField(max_length=250)
	years_lived = models.CharField('Years lived in',max_length=250)
	security_deposit = models.IntegerField(default=0)

class Landlord(models.Model):
	name_text = models.CharField(max_length=200)

# Create your models here.
