from django.contrib.auth.models import User
from django.db import models

from blogs.models import Blog


class Comment(models.Model):
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Comments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='Blogs')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner) + " |==> " + str(self.content)
