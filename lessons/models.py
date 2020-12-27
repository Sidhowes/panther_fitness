from django.db import models


class Lesson(models.Model):

    class Meta:

        verbose_name_plural = 'Lesson'

    programme_name = models.CharField(max_length=100, null=True)
    week = models.DecimalField(max_digits=2, decimal_places=0, null=True)
    day_1 = models.TextField(max_length=1000, null=True)
    day_2 = models.TextField(max_length=1000, null=True)
    day_3 = models.TextField(max_length=1000, null=True)
    day_4 = models.TextField(max_length=1000, null=True)
    day_5 = models.TextField(max_length=1000, null=True)
    day_6 = models.TextField(max_length=1000, null=True)
    day_7 = models.TextField(max_length=1000, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    