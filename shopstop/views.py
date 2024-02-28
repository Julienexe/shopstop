from django.shortcuts import render

<<<<<<< HEAD

=======
# Create your views here.
from django.shortcuts import render
>>>>>>> e4ad94230666d002f4690cd9ab1ccb4dd8ede7c1
from django.http import HttpResponse
from django.template import loader

def service_management(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())

def menu_management(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())

def business_register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

