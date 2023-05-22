from django.db import models

class Clients(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class Vehicle(models.Model):

    COLORS = (
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('black', 'Black'),
        ('white', 'White'),
    )

    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20)
    color = models.CharField(max_length=20, choices=COLORS)
    creation = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
        #return self.name

class VehiclePhotos(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vehicle_photos')

    #def __str__(self):
       # return self.name

class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    #def __str__(self):
        #return self.name
    
class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=50)

    #def __str__(self):
        #return self.name

class Appointment(models.Model):
    customer = models.ForeignKey(Clients, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    package = models.ForeignKey(Services, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=20)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    #def __str__(self):
        #return self.name







