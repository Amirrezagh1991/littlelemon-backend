from django.db import models


# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField(default=6)
    BookingDate = models.DateField()

    def __str__(self):
        return self.Name


# Add code to create Menu model
class Menu(models.Model):
   Title = models.CharField(max_length=255)
   Price = models.DecimalField(max_digits=10, decimal_places=2)
   Inventory = models.SmallIntegerField(default=5)

   def get_item(self):
       return f'{self.Title} : {str(self.Price)}'