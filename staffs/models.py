from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='staffs/avatars')
    email = models.EmailField(max_length=200)
    twitter = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name