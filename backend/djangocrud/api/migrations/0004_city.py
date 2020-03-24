# Generated by Django 3.0.3 on 2020-03-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('city_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
    ]
