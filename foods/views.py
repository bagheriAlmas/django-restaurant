from django.shortcuts import render, get_object_or_404

from foods.models import Food, Gallery


def food_list(request):
    foods = Food.objects.all()
    pictures = Gallery.objects.all()
    return render(request, 'foods/food_list.html', {'foods': foods, 'pictures': pictures})


def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'foods/food_detail.html', {'food': food})


def gallery_list(request):
    pictures = Gallery.objects.all()
    return render(request, 'partials/_gallery.html', {'pictures': pictures})
