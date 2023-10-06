from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.

# create user profile for both and staff developer

class UserProfile(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name}"

# message description sent to staff and sender info
class Message(models.Model):
    description=models.TextField()
    user_name= models.ForeignKey(UserProfile,related_name="sender", on_delete=models.CASCADE)
    staff_name= models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="reciever")
    time_taken=models.TimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    time_stamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" TO: {self.staff_name} from: {self.user_name}"
    
    class Meta():
        ordering = ('time_stamp',)


class Customers(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    customer = models.IntegerField()

    def __str__(self):
        return f"{self.customer}"
    