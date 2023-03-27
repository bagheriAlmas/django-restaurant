import uuid

from django.db import models


def image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return 'food/{}-{}.{}'.format(instance.name, uuid.uuid4().hex, ext)


class Food(models.Model):
    FOOD_CATEGORY = [
        ('breakfast', 'Breakfast'),
        ('drinks', 'Drinks'),
        ('main', 'Main'),
    ]

    RATE_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=15, choices=FOOD_CATEGORY, default='main')
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=0, )
    price = models.PositiveSmallIntegerField()
    time_prepare = models.PositiveSmallIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=image_upload_to)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='foods/gallery')
    is_enabled = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
