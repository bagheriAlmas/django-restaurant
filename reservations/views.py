from django.shortcuts import render

from reservations.forms import ReservationForm, ContactUsForm


def reserve_view(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            data = {
                'name': form.data['name'],
                'email': form.data['email'],
                'date': form.data['date'],
                'time': form.data['time'],
            }
            return render(request, 'pages/reservation_complete.html', {'form': data})

    else:
        form = ReservationForm()
    return render(request, 'pages/reservation.html', {'form': form})


def contact_us_view(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            data = {
                'name': form.data['name'],
                'email': form.data['email'],
            }
            return render(request, 'pages/contact_us_complete.html', {'data': data})

    else:
        form = ContactUsForm()
    return render(request, 'pages/contact_us.html', {'form': form})
