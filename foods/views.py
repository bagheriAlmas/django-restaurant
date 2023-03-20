from django.shortcuts import render

from foods.models import Food


def food_list(request):
    foods = Food.objects.all()
    return render(request, 'foods/food_list.html', {'foods': foods})
