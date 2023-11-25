from django import forms
from .models import Booking
from django.forms import TextInput, Select, Textarea
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email','mobile','doctor','booked','time','decs']
        widgets = {
            'name':TextInput(attrs={
                "type":"text",
                 'class':"form-control border-0",
                  'placeholder':"Your Name",
                  'style':"height: 55px"
            }),
            'email':TextInput(attrs={
                "type":"text",
                'class':"form-control border-0",
                'placeholder':"Your Email",
                'style':"height: 55px"
            }), 
            'mobile':TextInput(attrs={
                "type":"text",
                'class':"form-control border-0",
                'placeholder':"Your Phone",
                'style':"height: 55px"
            }), 
                'doctor':Select(attrs={
                'class':"form-control border-0",
                'placeholder':"Choose Doctor",
                'style':"height: 55px; background-color:white"
            }), 
                'booked':TextInput(attrs={
                "type":"date",
                'class':"form-control border-0",
                'placeholder':"Select Date",
                'style':"height: 55px"
            }), 
                'time':TextInput(attrs={
                "type":"time",
                'class':"form-control border-0",
                'placeholder':"Select Time",
                'style':"height: 55px"
            }), 
                'decs':Textarea(attrs={
                "type":"textarea",
                "class":"form-control border-0", 
                "rows":"5",
                "placeholder":"Describe your problem"
            }), 
        }
