import uuid

from django.db import models


def food_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return 'foods/{}-{}.{}'.format(instance.name, uuid.uuid4().hex, ext)


def gallery_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    if instance.type == 'Banner':
        return 'foods/gallery/{}-{}.{}'.format(instance.title, uuid.uuid4().hex, ext)
    else:
        return 'foods/banner/{}-{}.{}'.format(instance.title, uuid.uuid4().hex, ext)


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
    photo = models.ImageField(upload_to=food_image_upload_to)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    IMAGE_TYPE = [
        ('banner', 'Banner'),
        ('gallery', 'Gallery'),
    ]
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=gallery_image_upload_to)
    is_enabled = models.BooleanField(default=True)
    type = models.CharField(max_length=10, choices=IMAGE_TYPE, default='Gallery')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
