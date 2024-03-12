from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Service, Item, Business


def business_management(request, business_id):
    business = Business.objects.get(id = business_id)
    services = business.service_set.order_by("date_added")
    items = business.item_set.order_by("date_added")
    context = {"services":services, "items":items, "business" : business}

    # return render(request,'shop/business-admin.html', context)
    

def home(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/about_us.html')

def service_management(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())

def menu_management(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())

def business_register(request):
    template = loader.get_template( 'register.html')
    return HttpResponse(template.render() )

