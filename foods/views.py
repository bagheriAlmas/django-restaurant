from django.shortcuts import render, get_object_or_404

from foods.models import Food, Gallery


def special_food_list(request):
    foods = Food.objects.all()
    pictures = Gallery.objects.all().filter(type='gallery')
    banners = Gallery.objects.all().filter(type='banner')
    return render(request, 'foods/food_list.html', {'foods': foods, 'pictures': pictures, 'banners': banners})


def menu_list(request):
    foods = Food.objects.all()
    return render(request, 'foods/food_menu.html', {'foods': foods,})


def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'foods/food_detail.html', {'food': food})