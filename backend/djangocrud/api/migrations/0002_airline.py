# Generated by Django 3.0.3 on 2020-03-18 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('airline_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('airline_name', models.CharField(blank=True, max_length=30, null=True)),
                ('airline_iata', models.CharField(blank=True, max_length=2, null=True)),
                ('airline_icao', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'airline',
                'managed': False,
            },
        ),
    ]
