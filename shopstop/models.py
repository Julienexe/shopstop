from django.db import models

# Create your models here.
class List_of_businesses(models.Model):   #List of businesses
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length = 500)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Menu(models.Model):     #items on the menu list with their corresponding prices
    business = models.ForeignKey(List_of_businesses, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    price = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f'{ self.item_name}'
    
    
class Service_management(models.Model):
    business = models.ForeignKey(List_of_businesses, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255)
    price = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f' {self.service_name}'
    
class Business_photos_videos(models.Model):
    business = models.ForeignKey(List_of_businesses, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='photos/', blank = True) 
    videos = models.FileField(upload_to='videos/', blank = True) 

    def __str__(self):
        return f'{self.business}'  
