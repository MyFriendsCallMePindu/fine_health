# Create your views here.
from django.shortcuts import render, redirect
from .forms import AppointmentForm

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = AppointmentForm()

    return render(request, 'booking.html', {'form': form})


def booking_success(request):
    return render(request, 'booking_success.html')
