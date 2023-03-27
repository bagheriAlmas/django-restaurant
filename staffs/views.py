from django.shortcuts import render

from staffs.models import Staff


def staff_list_view(request):
    staffs = Staff.objects.all()
    return render(request, 'pages/staffs.html', {"staffs": staffs})
