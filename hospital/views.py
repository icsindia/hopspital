from django.shortcuts import render
from django.http import HttpResponse
from . forms import BookingForm
from . models import Department, Doctore

def index(request):
    form=BookingForm()
    department=Department.objects.all()
    doctor=Doctore.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
            return render(request,"index.html",{"form":form})
    context = {
        'form':form,
        'department':department,
        'doctor':doctor
    }      
    return render(request,"index.html",context)
