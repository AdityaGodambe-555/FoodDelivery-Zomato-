from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# Create your views here.
            
def user_register(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        uemail=request.POST['uemail']
       
        context={}
        if uname=='' or upass=='' or uemail=='':
            context['msg']='Fields cannot be Empty'
            return render(request,'authapp/register.html',context)
        elif upass!=ucpass:
            context['msg']='Password Doesnot Match'
            return render(request,'authapp/register.html',context)
        else:
            u=User.objects.create(username=uname,email=uemail)
            u.set_password(upass)
            u.save()
            context['msg']='User Created Sucessfully, Please Login'
            return render(request,'authapp/register.html',context)      
    else:
        return render(request,'authapp/register.html')
    
def user_login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        context={}
        if uname=='' or upass=='':
            context['errmsg']="Fields cannot be Blank"
            return render(request,'authapp/login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            if u is not None:
                login(request,u)
                return redirect('/dashboard')
            else:
                context={}
                context['errmsg']="Invalid username And Passowrd"
                return render(request,'authapp/login.html',context)

    else:
        return render(request,'authapp/login.html')
    
def user_logout(request):
    logout(request)
    return redirect('/')
        