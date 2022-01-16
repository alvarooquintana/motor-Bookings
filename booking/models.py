from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid





class Booking(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateTimeField(auto_now=True)
    date_booking = models.DateTimeField()
    phone = PhoneNumberField(blank= False, null = False)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.date_booking},{self.phone},{self.email}"

