from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from .forms import ProductForm,CategoryForm
from django.conf import settings
#send mail
from django.core.mail import send_mail


# Create your views here.
def getAllProducts(request):
    products = Product.objects.all().values()
    return render(request,'product/allProducts.html',{'products':products})


    #products = Product.objects.all()
    #products = Product.objects.all().values()
    #products = Product.objects.all().values('pName','pPrice')
    #products = Product.objects.all().values_list()
    #products = Product.objects.all().values_list('pName','pPrice')

    
    #product = Product.objects.filter(pPrice__gt=800).values()
    #product = Product.objects.filter(pPrice__gte=800).values()
    #product = Product.objects.filter(pPrice__lt=800).values()
    #product = Product.objects.filter(pPrice__lte=800).values()
    #product = Product.objects.filter(pName__startwith='m').values()
    #product = Product.objects.filter(pName__istartwith='m').values()
    #product = Product.objects.filter(pName__endwith='m').values()
    #product = Product.objects.filter(pName__iendwith='m').values()
    #product = Product.objects.filter(pName__contains='z').values()
    #product = Product.objects.filter(pName__icontains='z').values()

    #product = Product.objects.all().order_by('pPrice').values()
    #product = Product.objects.all().order_by('-pPrice').values()
    #product = Product.objects.all().order_by('pName').values()
    #product = Product.objects.all().order_by('-pName').values()

    
    
def addProducts(request):
    product = Product(pName="laptop",pPrice=98000,pQty=12,pDesc="dfnsnf",pStatus=True,pColor="Black")
    product.save()
    print ("Product Added")
    return render (request,'product/addProducts.html')

def deleteProduct(request,id):
    #id = 11
    products = Product.objects.get(id=id)
    products.delete()
    return HttpResponse("Product Deleted")


def updateProduct(request,id):
    product = Product.objects.get(id=id)
    product.pName = "Lenovo Laptop"
    product.pPrice = 55000
    product.pColor = "Silver (off Grey)"
    product.save()
    return HttpResponse("Product Updated")

def getProductDetail(request,id):
    product = Product.objects.get(id=id)    
    return render(request,'product/productdetail.html',{'product':product})

# crud operation with form

def addProductWithForm(request):
    
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
        return HttpResponse("product added")      
    return render(request,'product/addproductwithform.html',{'form':form}) 

    # if request.method == "POST":
    #     pName = request.POST['pName']

def updateProductWithForm(request,id):
    product = Product.objects.get(id=id)
    form = ProductForm()
    
    print("post.....")
    form = ProductForm(request.POST or None,instance=product)    
    if form.is_valid():
        form.save()
        return redirect('getproducts')  
    return render(request,'product/updateproductwithform.html',{'form':form})  


# category class 

def addCategory(request):
    form = CategoryForm()
    if request.method =="POST":
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('getcategories')
    return render(request,'product/addcategory.html',{'form':form})    

def getAllCategories(request):
    categories = Category.objects.all().values()
    return render(request,'product/allcategories.html',{'categories':categories})
                
   
def deleteCategory(request,id):
    cat = Category.objects.get(id=id)
    cat.delete()
    return redirect('getcategories')
        
    
def updateCat(request,id):
    cat = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None,instance=cat)
    if form.is_valid():
        cat.save()
        return redirect('getcategories')
    return render(request,'product/updatecategory.html',{'form':form})
        
def sendMail(request):
    subject = "welcome to django"
    message = "hello django"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mr.genius0180@gmail.com','pusadadiya1308@gmail.com']
    res = send_mail(subject,message,email_from,recipient_list)
    if res>0:
        print("mail sent")
    else:
        print("mail not sent")    
    print(res)
    return HttpResponse("mail sent")
