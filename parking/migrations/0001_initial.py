# Generated by Django 5.1.4 on 2024-12-10 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(default='Nairobi', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.CharField(max_length=50)),
                ('available', models.BooleanField(default=True)),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=6)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.location')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('parking_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingspace')),
            ],
        ),
    ]
