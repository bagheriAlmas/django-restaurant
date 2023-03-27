from django.contrib import admin
from foods.models import Food,Gallery


class FoodAdmin(admin.ModelAdmin):
    model = Food
    list_display = ('name', 'category')


class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ('title', 'is_enabled')


admin.site.register(Food,FoodAdmin)
admin.site.register(Gallery,GalleryAdmin)
