from django.db import models


class Fitness(models.Model):

    class Meta:

        verbose_name_plural = 'Fitness'
        ordering = ('day',)

    programme_name = models.CharField(max_length=100, null=True)
    week = models.DecimalField(max_digits=2, decimal_places=0, null=True)
    day = models.DecimalField(max_digits=2, decimal_places=0, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)
