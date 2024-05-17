from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator # This is for star rating

#Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=250)
    year = models.IntegerField()
    
class Airline(models.Model):
    airline_id = models.CharField(primary_key=True, max_length=3)
    airline_name = models.CharField(max_length=30, blank=True, null=True)
    airline_iata = models.CharField(max_length=2, blank=True, null=True)
    airlinepy_icao = models.CharField(max_length=3, blank=True, null=True)

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
    country = models.ForeignKey(Country, on_delete=models.CASCADE,default="")

    class Meta:
        managed = False
        db_table = 'city'


class Terminal(models.Model):
    terminal_id = models.IntegerField(primary_key=True)
    terminal_name = models.CharField(max_length=3, blank=True, null=True)



class Restaurant(models.Model):
    """
    How the image will be loaded ?
    API will give us URL and we will execute it in the front-end ?
    Dropping the Route and Cuisine type is a good  idea ?
    Cuisine type is no longer a foreign key

    """
    restaurant_id = models.CharField(primary_key=True, max_length=5)
    restaurant_name = models.CharField(max_length=20, blank=True, null=True)
    before_security = models.BooleanField(blank=True, null=True)
    cusine_type = models.CharField(max_length=20, blank=True, null=True)
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE,blank=True, null=True)
    #cuisine_type = models.ForeignKey('c', models.DO_NOTHING, db_column='cuisine_type', blank=True, null=True)
    #route = models.ForeignKey('Route', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def no_of_ratings(self):
        #How many times Restaurant rated by user
        ratings = RestaurantRating.objects.filter(restaurant=self)
        return len(ratings)
    
    def avg_rating(self):
        #This is average of all ratings
        sum = 0
        ratings = RestaurantRating.object.filter(restaurant=self)
        for r in ratings:
            sum += r.star
            if len(ratings) > 0:
                return sum / len(ratings)
            else:
                return 0


class RestaurantRating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=100, blank=True, null= True)

    class Meta:
        unique_together = (('user', 'restaurant'))
        index_together = (('user', 'restaurant'))
