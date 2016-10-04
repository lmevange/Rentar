from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Apartment(models.Model):
	address_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date added')
	def __str__(self):
		return self.question_text

class Landlord(models.Model):
	landlord_name = models.CharField(max_length=200)
	apartments = models.ForeignKey(Apartment, on_delete=models.CASCADE)
	def __str__(self):
		return self.landlord_name
