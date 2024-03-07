from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Repas(models.Model):
     x=[
        ('Pizza','Pizza'),
        ('Mlawi','Mlawi'),
        ('Tacos','Tacos'),
        ('Bagette','Bagette'),
        ('Ma9loub','Ma9loub'),
        ('Sandwitch','Sandwitch'),
        ('Crepe sucree','Crepe sucree'),
        ('Crepe sallée','Crepe sallée'),
]
     name = models.CharField(max_length=200,default="",blank=False)
     description = models.TextField(max_length=1000,default="",blank=False)
     price = models.DecimalField(max_digits=5, decimal_places=3)
     category=models.CharField(max_length=50,null=True,blank=True,choices=x)
     ratings = models.DecimalField(max_digits=3,decimal_places=2,default=0)
     stock = models.IntegerField(default=0)
     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

     def __str__(self):
        return self.name
class Review(models.Model):
    repas = models.ForeignKey(Repas, null=True, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=1000,default="",blank=False) 
    createAt = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.comment