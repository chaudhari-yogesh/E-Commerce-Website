import json
from math import ceil
from django.shortcuts import render, HttpResponse
from shop.models import Contact, OrderUpdate, Orders, Product

# Create your views here.

def index(request):
    
    productData= Product.objects.all()
    allproducts=[]
    catprods= Product.objects.values("category","id")
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides= n//4+ ceil((n/4)-(n//4))
        allproducts.append([prod, range(1, nSlides), nSlides])
    param={"allprod":allproducts}
    return render(request, "shop/index.html", param)

    #param= {"no_of_slide":nslides, "range":range(1,nslides),"product":productData}
    # allproducts= [[productData,range(1, len(productData)),nslides],[productData,range(1, len(productData)),nslides]]

def searchMatch(query, item):
    
    if query in item.product_name.capitalize() or query in item.product_name.lower() or query in item.desc.lower():
        return True
    else:
        return False
def search(request):
    query= request.GET.get("search")
    allproducts=[]
    catprods= Product.objects.values("category","id")
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        prod2= [item for item in prod if searchMatch(query, item)]
        n=len(prod)
        nSlides= n//4+ ceil((n/4)-(n//4))
        if len(prod2)!=0:
            allproducts.append([prod, range(1, nSlides), nSlides])
    param={"allprod":allproducts,"msg":""}
    # if len(allproducts)==0 or len(query)<4:
    #         param={"msg":"Please check your products name"}
    return render(request, "shop/search.html", param)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    if request.method=="POST":
        name= request.POST.get("name")
        gmail= request.POST.get("gmail")
        phonenumber= request.POST.get("phonenumber")
        txtarea= request.POST.get("txtarea")
        address= request.POST.get("address")

        contact= Contact(name=name,gmail=gmail, phonenumber=phonenumber, txtarea=txtarea,address=address)
        contact.save()

    return render(request,"shop/contact.html");


def productView(request, myid):
    product= Product.objects.filter(id=myid);
    print(product)
    
    return render(request, "shop/productView.html",{"products":product[0]});

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        gmail=request.POST.get('gmail', '')
        amount=request.POST.get('amount','')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        mobilenumber=request.POST.get('mobilenumber', '')

        order=Orders(items_json=items_json,name=name, gmail=gmail,amount=amount, address=address, city=city, state=state, zip_code=zip_code,mobilenumber=mobilenumber);
        order.save();
        update=OrderUpdate(order_id= order.order_id, update_desc="Your Order has been placed and shipped")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request,"shop/checkout.html")

def tracker(request):
    if request.method=="POST":
        orderid= request.POST.get('orderid','')
        gmail=request.POST.get('gmail','')
        try:
            order=Orders.objects.filter(order_id=orderid,gmail=gmail)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response= json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')


    return render(request,"shop/tracker.html")

def blog(request):
    return render(request,"shop/blog.html")