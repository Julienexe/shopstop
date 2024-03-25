from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import ItemModelForm


def business_management(request, business_id):
    business = Business.objects.get(id = business_id)
    services = business.service_set.order_by("date_added")
    items = business.item_set.order_by("date_added")
    context = {"services":services, "items":items, "business" : business}

    return render(request,'shop/business-admin.html', context)

def add_item(request):
    business = Business.objects.get(owner = request.user)
    if request.method == 'POST': # If the form has been submitted...
        form = ItemModelForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            item_name = form.cleaned_data['item_name']
            price = form.cleaned_data['price']
            photos = form.cleaned_data['photos']

            item = Item.objects.create(
                business =  business,
                item_name = item_name,
                price = price,
                photos = photos 
            )
            item.save()
            return redirect('shop:shop')
    else: 
        form = ItemModelForm() # An unbound form
    
    return render(request, 'shop/product/add-item.html', {'form': form})

    
def shop(request):
        items = Item.objects.all()
        services = Service.objects.all()
        context = {'items':items,'services':services}
        return render(request, "shop/home.html", context)

def product_detail(request, item_id):
     item = Item.objects.get(id = item_id)
     return render(request, 'shop/product/product_detail.html', {'item':item})

def home(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/about_us.html')

def service_management(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())

def menu_management(request):
    template = loader.get_template('shop/menu.html')
    context = {'list':[1,2,3,4]}
    return HttpResponse(template.render())

def business_register(request):
    template = loader.get_template( 'register.html')
    return HttpResponse(template.render() )

def business_profile(request):
    return render(request,'shop/business-profile-page.html')





