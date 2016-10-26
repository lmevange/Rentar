from django.db import models

class Apartment(models.Model):
	#location info
	address_full = models.CharField(max_length=250,primary_key=True)
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
	parking_onstreet = models.BooleanField(default=False)
	parking_offstreet = models.BooleanField(default=False)
	#public transportation
	public_transportation= models.BooleanField(default=False)
	#pets later add average fees
	pets = models.booleanField(default=False)
	#landlord info
	landlord = models.Foreignkey(LandLord) #should only have one
	#rating info
	ratings = models.ManyToManyField(Apartment_Ratings)

	avg_security_deposit = models.DecimalField(max_digits=5, decimal_places=2)
	avg_rent = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
	   return self.address_full

##################
#id with auto inc is set as primary key automatically for all tables
##################

class Landlord(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	def __str__(self):
	   return self.last_name
	
class Apartment_Rating(models.Model):
	#info on rent
	apartment = models.Foreignkey(Apartment, on_delete=models.CASCADE) #if apartment is deleted delete this too
	landlord = models.Foreignkey(Landlord)

	move_in_date = models.DateField()
	years_lived = models.PositiveSmallIntegerField(default=1)
	#costs
	starting_rent = models.DecimalField(max_digits=5, decimal_places=2)
	ending_rent = models.DecimalField(max_digits=5, decimal_places=2)
	security_deposit = models.DecimalField(max_digits=5, decimal_places=2)
	pet_fee = models.DecimalField(max_digits=5, decimal_places=2, default= 0)
	#ratings
	#utilities:
	water = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	heat = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	electric = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	garbage = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	#general
	parking = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	#changed from privacy
	neighborhood = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	location = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	maintenance = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	landlord = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	comment = models.TextField(max_length = 2000)
	def __str__(self):
	   return "Rating: " +id +" for " + apartment

class Landlord_Rating(models.Model)
	landlord = models.Foreignkey(Landlord, on_delete=models.CASCADE)
	apartment = models.Foreignkey(Apartment)
	#ratings
	hot = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	privacy = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	responsiveness = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	maintenance= models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	likeability = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True)
	def __str__(self):
	   return "Rating: " +id +" for " + landlord