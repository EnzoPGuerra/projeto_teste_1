# Generated by Django 4.2.1 on 2023-05-22 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('license_plate', models.CharField(max_length=20)),
                ('color', models.CharField(choices=[('blue', 'Blue'), ('red', 'Red'), ('yellow', 'Yellow'), ('green', 'Green'), ('black', 'Black'), ('white', 'White')], max_length=20)),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clients')),
            ],
        ),
        migrations.CreateModel(
            name='VehiclePhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='vehicle_photos')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_time', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clients')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.services')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.staff')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.vehicle')),
            ],
        ),
    ]
