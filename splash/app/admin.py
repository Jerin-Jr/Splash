from django.contrib import admin
from.models import service,Category,Booking

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','c_name','c_phone','c_email','v_model','booking_date','booked_on')
admin.site.register(service)
admin.site.register(Category)
admin.site.register(Booking,BookingAdmin)

# Register your models here.
