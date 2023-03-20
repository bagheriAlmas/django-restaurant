from django.contrib import admin
from foods.models import Food


class FoodAdmin(admin.ModelAdmin):
    model = Food
    list_display = ('name', 'category')


admin.site.register(Food,FoodAdmin)
