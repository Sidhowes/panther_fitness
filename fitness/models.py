from django.db import models


class Fitness(models.Model):

    class Meta:

        verbose_name_plural = 'Fitness'
        ordering = ('day',)

    programme_name = models.CharField(max_length=100, null=True)
    week = models.DecimalField(max_digits=2, decimal_places=0, null=True)
    day = models.DecimalField(max_digits=2, decimal_places=0, null=True)
    body_type = models.CharField(max_length=254, null=True)
    description = models.TextField(max_length=500, null=True)
    video_url = models.CharField(max_length=200, null=True)