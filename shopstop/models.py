from django.db import models

class Business(models.Model):   #List of businesses registered
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length = 500)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return f'{self.name}'

class Item(models.Model):     #items on the menu list with their corresponding prices
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=255)
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add = True)
    availability = models.BooleanField(default=True)
    photos = models.ImageField(upload_to='photos/', blank = True)
    def __str__(self):
        return f'{ self.item_name}'
    
    
class Service(models.Model):  #services provided by certain businesses
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='services/', blank = True)
    date_added = models.DateTimeField(auto_now_add = True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f' {self.service_name}'
        
    
class Business_photos_videos(models.Model):  #Businesses can upload their photos and videos
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='photos/', blank = True) 
    videos = models.FileField(upload_to='videos/', blank = True) 

    def __str__(self):
        return f'{self.business}'  
