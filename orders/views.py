from django.shortcuts import render
from shopstop.models import Order, OrderItem, Item
from django.http import JsonResponse
import json


#views to create cart items
def cart(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user, complete = False)
        items = order.orderitem_set.all()
    else:    
        items=[]
        order ={'get_cart_total':0,'get_cart_items':0}
    context = {'items':items, 
               'order':order}
    return render(request,"shop/cart/cart.html", context)

def checkout(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user, complete = False)
        items = order.orderitem_set.all()
    else:    
        items=[]
        order ={'get_cart_total':0,'get_cart_items':0}
    context = {'items':items, 
               'order':order}
    return render(request,"shop/cart/checkout.html", context)

def update_item(request):
    data = json.loads(request.body)
    productId = data['product_id']
    action = data['action']

    customer = request.user
    product = Item.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item,created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == "add":
        order_item.quantity = (order_item.quantity+1)
    elif action == "remove":
        order_item.quantity = (order_item.quantity-1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse(action + ' complete', safe=False)
