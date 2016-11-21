from django.db import models
from django.contrib.auth.models import User

class Apartment(models.Model):
	#location info
	#address_full = models.CharField(default="",max_length=250,primary_key=True)
	address_line = models.CharField(default="",max_length=250)
	city = models.CharField(default="",max_length=250)
	state = models.CharField(default="",max_length=250)
	zipcode = models.CharField(default="",max_length=250)
	#generic info
	bedrooms = models.CharField(default="",max_length=250)
	bathrooms = models.CharField(default="",max_length=250)
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
	parking_onstreet = models.BooleanField(default=False)
	parking_offstreet = models.BooleanField(default=False)
	#public transportation
	public_transportation= models.BooleanField(default=False)
	#pets later add average fees
	pets = models.BooleanField(default=False)
	#landlord info
	landlord_first_name = models.CharField(default="", max_length=200)
	landlord_last_name = models.CharField(default="", max_length=200)
	landlord_company = models.CharField(default = "", max_length=200)

	#rating info
	#security_deposit = models.DecimalField(default=0,max_digits=5, decimal_places=2)
	#rent = models.DecimalField(default=0,max_digits=6, decimal_places=2)

	def __str__(self):
	   return self.address_line


##################
# id with auto inc is set as primary key automatically for all tables
##################
class Apartment_Rating(models.Model):
	#info on rent
	apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, blank=True) #if apartment is deleted delete this too
	#landlord = models.ForeignKey(Landlord)

	move_in_date = models.DateField()
	years_lived = models.PositiveSmallIntegerField(default=0)
	#costs
	starting_rent = models.DecimalField(default=0, max_digits=8, decimal_places=2)
	ending_rent = models.DecimalField(default=0, max_digits=8, decimal_places=2)
	security_deposit = models.DecimalField(default=0,max_digits=8, decimal_places=2)
	pet_fee = models.DecimalField(default=0, max_digits=5, decimal_places=2)
	#ratings
	#utilities:default=0,
	water = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)
	heat = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)
	electric = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)
	garbage = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)
	#general
	parking = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)
	#changed from privacy
	neighborhood = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)
	location = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)

	landlord_hot = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)
	landlord_privacy = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)
	landlord_responsiveness = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)
	landlord_maintenance= models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)
	comment = models.TextField(max_length = 400)
	def __str__(self):
	   return str(id)
