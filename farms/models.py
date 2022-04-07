from django.db import models
from django.urls import reverse

class Farm(models.Model):
    row = models.IntegerField()
    col = models.IntegerField()
    lat = models.DecimalField(max_digits=30, decimal_places=15)
    lng = models.DecimalField(max_digits=30, decimal_places=15)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})