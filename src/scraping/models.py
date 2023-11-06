from django.db import models
from .utils import *
# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Складское помещение', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True) #мб пустым

    class Meta:
        verbose_name = 'Складское помещение'
        verbose_name_plural = 'Складские помещения'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)

class Device(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Устройство', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)  # мб пустым

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)

class Information(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Модель оборудования')
    company = models.CharField(max_length=250, verbose_name='Производитель')
    description = models.TextField(verbose_name='Описание оборудования')
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE,
                                  verbose_name='Складское помещение')
    device = models.ForeignKey('Device', on_delete=models.CASCADE,
                               verbose_name='Устройство')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Модель оборудования'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.title
