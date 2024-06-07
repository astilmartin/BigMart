from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.models import contactdb
from Backend.models import categorydb, productdb
from django.contrib import messages

# Create your views here.
def main_page(request):
    return render(request,"index.html")

def category_page(request):
    return render(request,"category.html")

def details_page(request):
    if request.method=="POST":
        na=request.POST.get('name')
        de=request.POST.get('description')
        img=request.FILES['img']
        obj=categorydb(Name=na,Description=de,Image=img)
        obj.save()
        messages.success(request, "saved successfully...")
        return redirect(category_page)

def show_category(request):
    data=categorydb.objects.all()
    return render(request,"show_category.html",{'data':data})

def edit_page(req,catid):
    data=categorydb.objects.get(id=catid)
    return render(req,"edit.html",{'data':data})

def update_category(request,catid):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('description')
        try:
            img=request.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=catid).Image
        categorydb.objects.filter(id=catid).update(Name=na,Description=de,Image=file)
        messages.success(request, "Updated successfully...")
        return redirect(show_category)


def delete_category(req,catid):
    x=categorydb.objects.filter(id=catid)
    x.delete()
    messages.error(req, "Deleted..!")
    return redirect(show_category)


def login_page(request):
    return render(request,"userlogin.html")


def admin_login(request):
    if request.method=="POST":
        un=request.POST.get("username")
        pa=request.POST.get("password")
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pa)
            if x is not None:
                login(request,x)
                request.session["username"] = un
                request.session["password"] = pa
                messages.success(request,"Login successful")
                return redirect(main_page)
            else:
                messages.error(request,"Invalid Password")
                return redirect(login_page)
        else:
            messages.warning(request,"User not found")
            return redirect(login_page)


def admin_logout(request):
    del request.session["username"]
    del request.session["password"]
    messages.success(request,"Logout successful")
    return redirect(login_page)


def pro_page(req):
    cat=categorydb.objects.all()
    return render(req,"products.html",{'cat':cat})

def pdetails_page(request):
    if request.method=="POST":
        cat=request.POST.get('cate')
        p_na=request.POST.get('pname')
        pr=request.POST.get('price')
        p_de=request.POST.get('pdescription')
        p_img=request.FILES['pimg']
        obj=productdb(Category=cat,Product_Name=p_na,Product_price=pr,P_Description=p_de,Product_Image=p_img)
        obj.save()
        messages.success(request,"Product saved successfully...!")
        return redirect(pro_page)

def show_products(request):
    data=productdb.objects.all()
    return render(request,"show_products.html",{'data':data})

def edit_product(req,proid):
    data=productdb.objects.get(id=proid)
    cat=categorydb.objects.all()
    return render(req,"editp.html",{'data':data,'cat':cat})

def update_products(request,proid):
    if request.method == "POST":
        ca = request.POST.get('cname')
        pn = request.POST.get('p_name')
        pp = request.POST.get('price')
        pd = request.POST.get('p_description')
        try:
            img=request.FILES['p_img']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=proid).Product_Image
        productdb.objects.filter(id=proid).update(Category=ca,Product_Name=pn,Product_price=pp,P_Description=pd,Product_Image=file)
        messages.success(request, "Updated successfully...")
        return redirect(show_products)


def delete_products(req,proid):
    x=productdb.objects.filter(id=proid)
    x.delete()
    messages.error(req,"Deleted successfully..!")
    return redirect(show_products)


def contact_data(request):
    data=contactdb.objects.all()
    return render(request,"contactpage.html",{'data':data})

def delete_contact(req,conid):
    x=contactdb.objects.filter(id=conid)
    x.delete()
    return redirect(contact_data)