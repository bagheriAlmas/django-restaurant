from django.shortcuts import render

from reservations.forms import ReservationForm


def reserve_view(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    return render(request, 'pages/reservation.html', {'form':form})
