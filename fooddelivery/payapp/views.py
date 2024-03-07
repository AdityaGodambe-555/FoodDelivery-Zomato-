from django.shortcuts import render
from payapp.models import Order
from payapp.models import OrderItem
from cartapp.models import Cart
import razorpay
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
        

    
def pay(request):
    c=Cart.objects.filter(uid=request.user.id)
    sum=0
    for x in c:
        sum=sum+(x.pid.price*x.qty)

    # print(sum)
    tot=sum*100
    
    client = razorpay.Client(auth=("rzp_test_wE3V2tf6iIn1LM", "7aQSkvkNQpMFUyiksm2S442D"))

    data = { "amount": tot, "currency": "INR", "receipt": "order_rcptid_11" }
    
    payment = client.order.create(data=data)
    
    context={}
    
    context['payment']=payment
    
    qty=request.GET['co']
    total=request.GET['to']
    
    context['total']=total
    
    context['quantity']=qty

    return render(request,'payapp/payment.html',context)

def order_det(request):
    context={}
    c=Cart.objects.filter(uid=request.user.id)
    qt=Cart.objects.filter(uid=request.user).count()
    o=Order.objects.create(uid=request.user,order_id=request.GET['order_id'],count=qt,total=request.GET['tot'],paystat=1)
    o.save()
    order_instance = Order.objects.get(order_id=request.GET['order_id'])
    for x in c:
        oit=OrderItem.objects.create(order_id=order_instance,pid=x.pid,quantity=x.qty)
        
    c.delete()
    oit.save()
    
    qtf=Cart.objects.filter(uid=request.user).count()
    context['quantity']=qtf
    context['success']="Payment Done Successfully"
    context['uorderid']=order_instance
    
    #send Mail
    payid=request.GET['pay_id']
    orderid=request.GET['order_id']
    sign=request.GET['sign']
    # print(payid)
    # print(orderid)
    # print(sign)
    
    text_message = "Amount Paid: {} Order Placed Successfully. Your Payment ID: {} and Order ID: {}".format(request.GET['tot'], payid, orderid)
    
    html_message = render_to_string('payapp/email.html', {'tot': request.GET['tot'], 'payid': payid, 'orderid': orderid, 'uorderid': order_instance})
    
    # Create the email message
    msg = EmailMultiAlternatives(
    "Order Details",
    text_message,
    "godambeaditya@gmail.com",
    ["godambedhanshree@gmail.com"],
    )

    # Attach the HTML message
    msg.attach_alternative(html_message, "text/html")

    # Send the email
    msg.send()

    # msg="Amount Paid:"+ request.GET['tot'] +"Order Placed Successfully. Your Payment ID:"+payid+" and Order ID:"+orderid
    # send_mail(
    # "Order Details",
    # msg,
    # "godambeaditya@gmail.com",
    # ["godambedhanshree@gmail.com"],
    # fail_silently=False,
    # )
    
    

    return render(request,"payapp/payment.html",context)

def order_view(request):
    context={}
    order_instance = Order.objects.filter(uid=request.user)
    data_list=[]
    for x in order_instance:
        b=x.id
        order_items = OrderItem.objects.filter(order_id=b)
        data_list.extend(order_items)
        
    context['data'] = data_list
    qtf=Cart.objects.filter(uid=request.user).count()
    context['quantity']=qtf
    return render(request,"payapp/orders.html",context)
