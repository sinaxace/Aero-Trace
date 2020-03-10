from django.db import models

# # Create your models here.
# class Movie(models.Model):
#     title = models.CharField(max_length=32)
#     desc = models.CharField(max_length=250)
#     year = models.IntegerField()

# class city(models.Model):
#     city_id = models.CharField(max_length=4)
#     city_name = models.CharField(max_length=20)
#     country_id = models.CharField(max_length=4)

# class airline_info(models.Model):
#     airline_info_id = models.CharField(max_length=3)
#     airline_id = models.CharField(max_length=3)
#     terminal_id = models.CharField(max_length=3)
#     contact_no = models.CharField(max_length=15)
#     website = models.CharField(max_length=30)
#     counter_loaction_id = models.CharField(max_length=6)
#     route_id = models.CharField(max_length=6)

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Airline(models.Model):
    airline_id = models.CharField(primary_key=True, max_length=3)
    airline_name = models.CharField(max_length=30, blank=True, null=True)
    airline_iata = models.CharField(max_length=2, blank=True, null=True)
    airline_icao = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airline'


class AirlineInfo(models.Model):
    airline_info_id = models.CharField(primary_key=True, max_length=3)
    airline = models.ForeignKey(Airline, models.DO_NOTHING, blank=True, null=True)
    terminal = models.ForeignKey('Terminal', models.DO_NOTHING, blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    website = models.CharField(max_length=30, blank=True, null=True)
    counter_loaction_id = models.CharField(max_length=6, blank=True, null=True)
    route = models.ForeignKey('Route', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airline_info'


class ApiMovie(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=250)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_movie'


class Arrivals(models.Model):
    arr_guide_id = models.CharField(primary_key=True, max_length=5)
    arr_baggage_info = models.CharField(max_length=50, blank=True, null=True)
    arr_customs_immigration = models.CharField(max_length=50, blank=True, null=True)
    arr_airline = models.ForeignKey(Airline, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arrivals'


class ArrivalsDetails(models.Model):
    arr_detail_id = models.CharField(primary_key=True, max_length=5)
    arr_date = models.DateField(blank=True, null=True)
    arr_time = models.TimeField(blank=True, null=True)
    arr_status = models.ForeignKey('FlightStatus', models.DO_NOTHING, blank=True, null=True)
    arr_from_city = models.ForeignKey('City', models.DO_NOTHING, blank=True, null=True)
    airline = models.ForeignKey(Airline, models.DO_NOTHING, blank=True, null=True)
    flight_number = models.CharField(max_length=7, blank=True, null=True)
    arr_terminal = models.ForeignKey('Terminal', models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey('Route', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arrivals_details'


class ArrivalsGuideInfo(models.Model):
    arr_guide_id = models.CharField(primary_key=True, max_length=6)
    arr_guide_details = models.CharField(max_length=255, blank=True, null=True)
    airline = models.ForeignKey(Airline, models.DO_NOTHING, blank=True, null=True)
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING, blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)
    services = models.ForeignKey('Services', models.DO_NOTHING, blank=True, null=True)
    facility = models.ForeignKey('Facility', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arrivals_guide_info'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    city_id = models.CharField(primary_key=True, max_length=3)
    city_name = models.CharField(max_length=30, blank=True, null=True)
    country_id = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    country_id = models.CharField(primary_key=True, max_length=3)
    country_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class CrusinType(models.Model):
    crusintype_id = models.CharField(primary_key=True, max_length=5)
    cursinetype_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crusin_type'


class Departures(models.Model):
    dep_guide_id = models.CharField(primary_key=True, max_length=5)
    dep_baggage_info = models.CharField(max_length=50, blank=True, null=True)
    dep_security_security = models.CharField(max_length=50, blank=True, null=True)
    dep_security_us_customs = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departures'


class DeparturesDetails(models.Model):
    dep_detail_id = models.CharField(primary_key=True, max_length=5)
    dep_date = models.DateField(blank=True, null=True)
    dep_time = models.TimeField(blank=True, null=True)
    dep_status = models.ForeignKey('FlightStatus', models.DO_NOTHING, blank=True, null=True)
    dep_destination_city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    airline = models.ForeignKey(Airline, models.DO_NOTHING, blank=True, null=True)
    flight_number = models.CharField(max_length=7, blank=True, null=True)
    dep_terminal = models.ForeignKey('Terminal', models.DO_NOTHING, blank=True, null=True)
    gate = models.ForeignKey('Gate', models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey('Route', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departures_details'


class DeparturesGuideInfo(models.Model):
    dep_guide_info_id = models.CharField(primary_key=True, max_length=5)
    dep_guide_details = models.CharField(max_length=255, blank=True, null=True)
    airline = models.ForeignKey(Airline, models.DO_NOTHING, blank=True, null=True)
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING, blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)
    services = models.ForeignKey('Services', models.DO_NOTHING, blank=True, null=True)
    facility = models.ForeignKey('Facility', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departures_guide_info'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Facility(models.Model):
    facility_id = models.CharField(primary_key=True, max_length=5)
    facility_name = models.CharField(max_length=20, blank=True, null=True)
    route = models.ForeignKey('Route', models.DO_NOTHING, blank=True, null=True)
    required = models.ForeignKey('Passenger', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility'


class FlightStatus(models.Model):
    status_id = models.CharField(primary_key=True, max_length=3)
    status_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flight_status'


class Gate(models.Model):
    gate_id = models.IntegerField(primary_key=True)
    gate_naem = models.CharField(max_length=4, blank=True, null=True)
    route = models.ForeignKey('Route', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gate'


class Passenger(models.Model):
    customer_type_id = models.CharField(primary_key=True, max_length=5)
    customer_type_name = models.CharField(max_length=20, blank=True, null=True)
    purpose = models.CharField(max_length=20, blank=True, null=True)
    membership = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger'


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Restaurant(models.Model):
    restaurant_id = models.CharField(primary_key=True, max_length=5)
    restaurant_name = models.CharField(max_length=20, blank=True, null=True)
    before_security = models.BooleanField(blank=True, null=True)
    crusintype = models.ForeignKey(CrusinType, models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey('Route', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class ReviewsRestaurants(models.Model):
    review_id = models.CharField(primary_key=True, max_length=5)
    review_description = models.CharField(max_length=255, blank=True, null=True)
    belong_to = models.ForeignKey(Restaurant, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews_restaurants'


class ReviewsServices(models.Model):
    review_id = models.CharField(primary_key=True, max_length=5)
    review_description = models.CharField(max_length=255, blank=True, null=True)
    belong_to = models.ForeignKey('Services', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews_services'


class ReviewsShops(models.Model):
    review_id = models.CharField(primary_key=True, max_length=5)
    review_description = models.CharField(max_length=255, blank=True, null=True)
    belong_to = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews_shops'


class Route(models.Model):
    route_id = models.CharField(primary_key=True, max_length=6)
    loaction_id = models.CharField(max_length=6, blank=True, null=True)
    route = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route'


class Services(models.Model):
    services_id = models.CharField(primary_key=True, max_length=5)
    services_name = models.CharField(max_length=20, blank=True, null=True)
    before_security = models.BooleanField(blank=True, null=True)
    servicestype = models.ForeignKey('ServicesType', models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey(Route, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class ServicesType(models.Model):
    servicestype_id = models.CharField(primary_key=True, max_length=5)
    servicestype_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_type'


class Shop(models.Model):
    shop_id = models.CharField(primary_key=True, max_length=5)
    shop_name = models.CharField(max_length=20, blank=True, null=True)
    before_security = models.BooleanField(blank=True, null=True)
    shoptype = models.ForeignKey('ShopType', models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey(Route, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop'


class ShopType(models.Model):
    shoptype_id = models.CharField(primary_key=True, max_length=5)
    shoptype_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_type'


class Terminal(models.Model):
    terminal_id = models.IntegerField(primary_key=True)
    terminal_name = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terminal'
