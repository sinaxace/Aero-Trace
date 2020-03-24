from django.contrib import admin
from .models import Movie, Airline,Country,City
# Register your models here.
admin.site.register(Airline)
admin.site.register(Country)
admin.site.register(City)
