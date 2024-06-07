from django.contrib import messages
from django.shortcuts import render, redirect

from Backend.models import productdb, categorydb
from webapp.models import contactdb, registerdb, cartdb


# Create your views here.


def homepage(request):
    cat = categorydb.objects.all()
    return render(request,"home.html",{'cat':cat})

def aboutpage(request):
    cat = categorydb.objects.all()
    return render(request,"about.html",{'cat':cat})

def contactpage(request):
    cat = categorydb.objects.all()
    return render(request,"contact.html",{'cat':cat})

def Our_products(request):
    pro=productdb.objects.all()
    cat=categorydb.objects.all()
    return render(request,"OurProducts.html",{'product':pro,'cat':cat})

def save_contact(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        su=request.POST.get('sub')
        me=request.POST.get('message')
        obj=contactdb(Name=na,Email=em,Subject=su,Message=me)
        obj.save()
        return redirect(contactpage)

def filtered_products(request,cat_name):
    data=productdb.objects.filter(Category=cat_name)
    cat=categorydb.objects.all()
    return render(request,"products_filtered.html",{'data':data,'cat':cat})


def singlepage(request,proid):
    data=productdb.objects.get(id=proid)
    cat = categorydb.objects.all()
    pro=productdb.objects.all()
    return render(request,"single_product.html",{'data':data,'cat':cat,'pro':pro})


def register_page(request):
    return render(request,"Register.html")



def save_register(request):
    if request.method=="POST":
        us=request.POST.get('user')
        em=request.POST.get('email')
        pa=request.POST.get('pass')
        obj=registerdb(Username=us,Email=em,Password=pa)
        if registerdb.objects.filter(Username=us).exists():
            messages.warning(request,"Username already exists..!!")
            return redirect(register_page)
        elif registerdb.objects.filter(Email=em).exists():
            messages.warning(request,"Email ID already exists...!!")
            return redirect(register_page)
        else:
            obj.save()
            messages.success(request,"Registered Successfully..!!")
        return redirect(register_page)


def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pas=request.POST.get('password')
        if registerdb.objects.filter(Username=un,Password=pas).exists():
            request.session['Username']=un
            request.session['Password']=pas
            return redirect(homepage)
        else:
            return redirect(register_page)
    else:
        return redirect(register_page)


def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(homepage)


def save_cart(request):
    if request.method=="POST":
        qt=request.POST.get('qty')
        pr=request.POST.get('price')
        un=request.POST.get('uname')
        pn=request.POST.get('pname')
        obj=cartdb(Quantity=qt,TotalPrice=pr,Username=un,ProductName=pn)
        obj.save()
        messages.success(request, "Added to cart successful")
        return redirect(homepage)



def cartpage(request):
    data=cartdb.objects.filter(Username=request.session['Username'])
    cat = categorydb.objects.all()
    total=0
    for d in data:
        total=total+d.TotalPrice
    if total>500:
        delivery_charge=0
    else:
        delivery_charge=50
    final=total+delivery_charge
    return render(request,"cart.html",{'cat':cat,'data':data,'total':total,'delivery_charge':delivery_charge,'final':final})


def delete_item(req,pid):
    x=cartdb.objects.filter(id=pid)
    x.delete()
    messages.error(req,"Deleted successfully")
    return redirect(cartpage)

def user_login_page(request):
    return render(request,"userlogin.html")

