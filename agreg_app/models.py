from django.db import models
from django.utils import timezone

# Create your models here.


class Values(models.Model):
    name = models.CharField(max_length=15)
    value_buy = models.FloatField(null=True)
    value_sell = models.FloatField(null=True)
    value_nb = models.FloatField(null=True)
    time = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name}-{self.time}'

    class Meta:
        verbose_name = 'Данные по валюте'
        verbose_name_plural = 'Данные по валютам'
