from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import service,Category,Booking
from. forms import BookingForm,feedbackForm
from splash. settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
from django.contrib .auth.models import User
from django.contrib.auth import authenticate,login
import razorpay

def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def loginn(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Username")
    return render(request,'loginn.html')
def signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        my_user=User.objects.create_user(username=username,email=email,password=password)
        my_user.save()
        return redirect('loginn')
    return render(request,'signup.html')
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')
            
    
    form = BookingForm()

    dict_form={'form':form}
    return render(request,'booking.html',dict_form)
def services(request):
    dict_service={'service':service.objects.all()}
    return render(request,'services.html',dict_service)

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def payment(request):
     order_amount = 25000
     order_currency = 'INR'
     payment_order = client.order.create(dict(amount=order_amount,currency=order_currency,payment_capture= 1))
     payment_order_id = payment_order['id']
     
     context = {
        'amount':250,'api_key': RAZORPAY_API_KEY , 'order_id':payment_order_id
        }
     return render(request, 'payment.html',context)

def feedback(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'feedconform.html')
    form = feedbackForm()
    dict_form={'form':form}        
    return render(request,'feedback.html',dict_form)
def about(request):
    return render(request,'about.html')
def category(request):
    dict_category={'category':Category.objects.all()}
    return render(request,'category.html',dict_category)








