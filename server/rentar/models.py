from django.db import models

class Apartment(models.Model):
	address_text = models.CharField(max_length=250)
	move_in = models.DateField('Moved in')
	years_lived = models.PositiveSmallIntegerField('Years lived in')
	security_deposit = models.IntegerField(default=0)

	def __str__(self):
	   return self.address_text

class LandLord(models.Model):
	name_text = models.CharField(max_length=200)

	def __str__(self):
	   return self.name_text
	
