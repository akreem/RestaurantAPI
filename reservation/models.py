from django.db import models

from django.contrib.auth.models import User
from Repas.models import Repas


# Create your models here.
class PaymentStatus(models.TextChoices):
    PAID = 'Paid'
    UNPAID = 'Unpaid' 

class PaymentMode(models.TextChoices):
    COD = 'COD'
    CARD = 'CARD' 
class Reservation(models.Model):
    table_number = models.IntegerField()
    seats = models.IntegerField()
    phone_no = models.CharField(max_length=100, default="", blank=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    statutReservation = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=30, choices=PaymentStatus.choices, default=PaymentStatus.UNPAID)
    payment_mode = models.CharField(max_length=30, choices=PaymentMode.choices, default=PaymentMode.COD)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  
    repas = models.ForeignKey(Repas, null=True, on_delete=models.SET_NULL)
    createAt = models.DateTimeField(auto_now_add=True)

 
    def __str__(self):
        return f"Table {self.table_number} - Reservation by {self.user.username} on {self.createAt}"