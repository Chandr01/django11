from django.db import models


# Create your models here.

class Subscriber(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.CharField(max_length=100, verbose_name='Почта')
    # text = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ' комментариев'
