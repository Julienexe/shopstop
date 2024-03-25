from django.db import models
from users.models import CustomUser

#main app models
class Business(models.Model):   #List of businesses registered
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE,  blank=True, null = True)
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
    
    def imageURL(self):
        try:
            url = self.photos.url
        except:
            url = ''
        return url
    
    
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
    
class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete = models.SET_NULL, blank=True, null = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False, null=True, blank = True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Item,on_delete=models.SET_NULL, blank = True, null= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank = True, null = True)
    quantity = models.PositiveIntegerField(default=0, null=True,blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    @property
    def get_total(self):
        total = self.product.price *self.quantity
        return total