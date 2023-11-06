from django.db import models

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
            self.slug = from_cyrillic_to_end(str(self.name))
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