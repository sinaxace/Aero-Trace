from django.db import models

#Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=250)
    year = models.IntegerField()
    
class Airline(models.Model):
    airline_id = models.CharField(primary_key=True, max_length=3)
    airline_name = models.CharField(max_length=30, blank=True, null=True)
    airline_iata = models.CharField(max_length=2, blank=True, null=True)
    airline_icao = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airline'

class Country(models.Model):
    country_id = models.CharField(primary_key=True,max_length=3)
    country_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'

class City(models.Model):
    city_id=models.CharField(primary_key=True,max_length=3)
    city_name=models.CharField(max_length=30, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'city'

    