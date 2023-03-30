from django.shortcuts import render, get_object_or_404

from foods.models import Food, Gallery


def special_food_list_view(request):
    foods = Food.objects.all()
    pictures = Gallery.objects.all().filter(type='gallery',special=True)
    banners = Gallery.objects.all().filter(type='banner')
    return render(request, 'foods/food_list.html', {'foods': foods, 'pictures': pictures, 'banners': banners})


def menu_list_view(request):
    foods = Food.objects.all()
    return render(request, 'foods/food_menu.html', {'foods': foods,})


def food_detail_view(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'foods/food_detail.html', {'food': food})


def gallery_list_view(request):
    gallery = Gallery.objects.all().filter(type='gallery')
    return render(request, 'pages/gallery.html', {'gallery': gallery})