from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, orderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nslides = n//4 + ceil(n/4 - (n//4))
    # used this for single slideshow
    # param = {'no_of_slides': nslides, 'range': range(1, nslides), 'products': products}
    # for showing more than one slideshow
    # all_prods = [[products, range(1, nslides), nslides],[products, range(1, nslides), nslides]]
    all_prods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil(n / 4 - (n // 4))
        all_prods.append([prod, range(1, nslides), nslides])
    param = {'all_prods': all_prods}

    return render(request, 'shop/index.html', param)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        # print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})


def tracker(request):
    if request.method == "POST":

        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        # return HttpResponse(f"{orderId} and {email}")
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = orderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
            # return HttpResponse(f'exception{e}')

    return render(request, 'shop/tracker.html')


def product_view(request, myid):
    # fetch the product view using the myid
    product = Product.objects.filter(id=myid)

    return render(request, 'shop/prodView.html', {'product': product[0]})


def search(request):
    return render(request, 'shop/search.html')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        # print(name, email, phone, desc)
        order = Orders(items_json=items_json, name=name, email=email, phone=phone, address=address, city=city,
                       state=state, zip_code=zip_code, amount=amount)
        print(items_json, name, email)
        order.save()
        update = orderUpdate(order_id=order.order_id, update_desc="The order has been place.")
        update.save()
        thank = True
        id = order.order_id
        # return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
        # Request Paytm to transfer the amount to your account after payment by user

    return render(request, 'shop/checkout.html')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    pass
