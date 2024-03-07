from django.shortcuts import render,redirect
from productsapp.models import Product
from django.db.models import Q
from cartapp.models import Cart

# Create your views here.
def home_page(request):
    return render(request,'productsapp/home.html')

def dashboard(request):
    if request.user.is_authenticated:
        context={}
        q1=Q(is_active=1)
        c=Product.objects.filter(q1)
        context['data']=c
        qt=Cart.objects.filter(uid=request.user).count()
        context['quantity']=qt
        return render(request,'productsapp/dashboard.html',context)
    else:
        return redirect('/authapp/login')

def filter_by_typ(request):
    q=request.GET['q']
    x=request.GET['x']
    q1=Q(is_active=1)
    q2=Q(f_type=q)
    q3=Q(cat=x)
    p=Product.objects.filter(q1 & q2 & q3)
    context={}
    context['data']=p
    return render(request,'productsapp/category.html',context)

def sort_by_price(request):
        q=request.GET['q']
        x=request.GET['x']
        if q=='0':
            col='price'
        else:
            col='-price'
        context={}
        q1=Q(cat=x)
        q2=Q(is_active=1)
        context['data']=Product.objects.order_by(col).filter( q1 & q2 )
        return render(request,'productsapp/category.html',context)
    
def filterbyrange(request):
    min=request.GET['min']
    max=request.GET['max']
    x=request.GET['x']
    q4=Q(cat=x)
    q1=Q(is_active=1)
    q2=Q(price__gte=min)
    q3=Q(price__lte=max)
    context={}
    context['data']=Product.objects.filter(q1 & q2 & q3 & q4)
    return render(request,'productsapp/category.html',context)

def Category_food(request):
    x=request.GET['q']
    q1=Q(is_active=1)
    q2=Q(cat=x)
    f=Product.objects.filter(q1 & q2)
    context={}
    context['data']=f
    if request.user.is_authenticated:
        qt=Cart.objects.filter(uid=request.user).count()
        context['quantity']=qt
    return render(request,"productsapp/category.html",context)

def search(request):
    query=request.GET['query']
    q2=Q(name__icontains=query)  
    q1=Q(is_active=1)
    f=Product.objects.filter(q1 & q2)
    
    # f=Product.objects.filter(q1 & q2)
    context={}
    context['data']=f
    context['query']=query
    if request.user.is_authenticated:
        qt=Cart.objects.filter(uid=request.user).count()
        context['quantity']=qt
    return render(request,"productsapp/search.html",context)
    
