from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    rate = models.SmallIntegerField(default=0)
    price = models.PositiveIntegerField()
    time_prepare = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='foods/')