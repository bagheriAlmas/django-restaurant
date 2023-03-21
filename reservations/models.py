from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    guests_num = models.PositiveSmallIntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name + " - " + self.phone
