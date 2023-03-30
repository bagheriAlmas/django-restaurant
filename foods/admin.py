from django.contrib import admin
from foods.models import Food, Gallery


class FoodAdmin(admin.ModelAdmin):
    model = Food
    list_display = ('name', 'category', 'special')
    ordering = ('special',)


class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ('title', 'is_enabled', 'type','special')
    list_filter = ('type',)
    ordering = ('-special',)



admin.site.register(Food, FoodAdmin)
admin.site.register(Gallery, GalleryAdmin)
