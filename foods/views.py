from django.shortcuts import render, get_object_or_404

from foods.models import Food


def food_list(request):
    foods = Food.objects.all()
    return render(request, 'foods/food_list.html', {'foods': foods})


def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'foods/food_detail.html', {'food': food})
