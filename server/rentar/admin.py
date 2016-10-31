from django.contrib import admin

from .models import Apartment, Landlord, Apartment_Rating, Landlord_Rating

admin.site.register(Apartment)
admin.site.register(Landlord)
admin.site.register(Apartment_Rating)
admin.site.register(Landlord_Rating)
# Register your models here.
