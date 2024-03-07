from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from productsapp.models import Product
from cartapp.models import Cart
from django.db.models import Q


# Create your views here.
def user_cart(request):
    if request.user.is_authenticated:
        context={}
        qt=Cart.objects.filter(uid=request.user).count()
        context['quantity']=qt
        d=Cart.objects.filter(uid=request.user)
        context['data']=d  
        sum=0
        for x in d:
            sum=sum+(x.qty*x.pid.price)
        context['total']=sum
        
        return render(request,'cartapp/cart.html',context)
    else:
        return redirect('/authapp/login')
    
def add_cart(request):
    context={}
    if request.user.is_authenticated:
        pid=request.GET['pid']
        user_id=request.user.id 
        uobj=User.objects.get(id=user_id)
        pobj=Product.objects.get(id=pid)        
        context['pid']=pid    
        z=int(request.GET['z'])
        try:
            q1=Q(uid=uobj)
            q2=Q(pid=pobj)
            c=Cart.objects.get(q1 & q2)
            context['vmsg']="Product alreay exists In the Cart"
                
        except Exception:
            c=Cart.objects.create(uid=uobj,pid=pobj)
            c.save()
            context['success']="Successfully added in the cart"
            
            
        if z == 0:
            x=request.GET['q']
            q1=Q(is_active=1)
            f=Product.objects.filter(q1)
            context['data']=f
            qt=Cart.objects.filter(uid=request.user).count()
            context['quantity']=qt
        
                    
            return render(request,'productsapp/dashboard.html',context)
            
        elif z==1:   
            x=request.GET['q']
            q1=Q(is_active=1)
            q2=Q(cat=x)
            f=Product.objects.filter(q1 & q2)
            context['data']=f
    
                
            qt=Cart.objects.filter(uid=request.user).count()
            context['quantity']=qt
            
                        
            return render(request,'productsapp/category.html',context)
        else :
            x=request.GET['q']
            q1=Q(is_active=1)
            query=request.GET['query']
            q3=Q(name__icontains=query) 
            f=Product.objects.filter(q1 & q3)
            context['data']=f
                
            qt=Cart.objects.filter(uid=request.user).count()
            context['quantity']=qt
            
            query=request.GET['query']
            context['query']=query
                        
            return render(request,'productsapp/search.html',context)
    
    
    else:
        return redirect('/authapp/login')    
    
    
def remove_cart(request):
    pid=request.GET['pid']
    q1=Q(pid=pid)
    q2=Q(uid=request.user.id)
    x = Cart.objects.get(q1 & q2)
    x.delete()

    context={}
    rt=Cart.objects.filter(uid=request.user)
    context['data']=rt
    
    qt=Cart.objects.filter(uid=request.user).count()
    context['quantity']=qt
    # return render(request,'cartapp/cart.html',context)
    return redirect("/cartapp/")

def update_qty(request):
    q=request.GET['q']
    cid=request.GET['cid']
    c=Cart.objects.filter(id=cid)
    if q=='1':
        temp=c[0].qty+1
    else:
        if c[0].qty>1:
            temp=c[0].qty-1
        else:
            temp=1
    c.update(qty=temp)
    return redirect('/cartapp/')