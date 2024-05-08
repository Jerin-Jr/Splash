from django import forms
from .models import Booking,feedback

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets={
            'booking_date' : DateInput(),
        }


        labels={
            'c_name':"Name:",
            'c_phone':"Phone Number:",
            'c_email':"Email:",
            'v_model':"Vehicle_Model:",
            'booking_date':"Booking_date",
        }
class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'