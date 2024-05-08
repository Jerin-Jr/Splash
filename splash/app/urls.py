from django.urls import path,include
from. import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('loginn',views.loginn,name='loginn'),
    path('signup',views.signup,name='signup'),
    
    path('booking',views.booking,name='booking'),
    path('services',views.services,name='services'),
    path('payment',views.payment,name='payment'),
    path('feedback',views.feedback,name='feedback'),
    path('about',views.about,name='about'),
    path('category',views.category,name='category'),
]
