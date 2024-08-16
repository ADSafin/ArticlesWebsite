from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    title = models.CharField('Название статьи', max_length=100)
    content = models.TextField('Статья')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img')

    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])