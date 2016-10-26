from django.db import models

class Apartment(models.Model):
	#location info
	full_address = models.CharField(max_length=250,primary_key=True)
	address_line = models.CharField(max_length=250)
	city = models.CharField(max_length=250)
	state = models.CharField(max_length=250)
	zipcode = models.CharField(max_length=250)
	#generic info
	bedrooms = models.CharField(max_length=250)
	bathrooms = models.CharField(max_length=250)
	living_room = models.BooleanField(default=False)
	dining_room = models.BooleanField(default=False)
	basement = models.BooleanField(default=False)
	attic = models.BooleanField(default=False)
	secondary_storage = models.BooleanField(default=False)
	#utilities included:
	water = models.BooleanField(default=False)
	heat = models.BooleanField(default=False)
	electric = models.BooleanField(default=False)
	garbage = models.BooleanField(default=False)
	#washer or dryer
	washer = models.BooleanField(default=False)
	dryer = models.BooleanField(default=False)
	#parking info
	parking_onstreet = models.BooleanField()
	parking_offstreet = models.BooleanField()
	#public transportation
	public_transportation= models.BooleanField()
	#add average rent and/or security deposit

	#landlord info (should only be on one table, chose this casue it is the form)
	landlords = models.ManyToManyField(LandLord)

	years_lived = models.PositiveSmallIntegerField('Years lived in')
	security_deposit = models.IntegerField(default=0)

	def __str__(self):
	   return self.address_line

class Landlord(models.Model):
	name_text = models.CharField(max_length=200)
	properties = models.
	def __str__(self):
	   return self.name_text
	
class Apartment_Rating(models.Model):
	