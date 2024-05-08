from django.db import models

# Create your models here.
class service(models.Model):
    service_name = models.CharField(max_length=255)
    service_description = models.CharField(max_length=355)
    service_price = models.IntegerField(default=0)

    def __str__(self):
        return(self.service_name)
    
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='vehicles', default='default_image.jpg')
    def __str__(self):
        return (self.category_name)    
    
class Booking(models.Model):
    c_name = models.CharField(max_length=255)
    c_phone = models.CharField(max_length=255) 
    c_email = models.EmailField() 
    v_model = models.CharField(max_length=255)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

class feedback(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Feedback = models.CharField(max_length=355)    
          

