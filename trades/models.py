from django.db import models
from django.urls import reverse


class Journal(models.Model):

    name = models.CharField(null=False, blank=False, max_length=255)

    def get_absolute_url(self):
        return reverse('trades:trade_view', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Trade(models.Model):

    strategy = models.CharField(null=False, blank=False, max_length=255)
    balance = models.IntegerField(null=False, blank=False, default=0)
    win_or_loss = models.CharField(null=False, blank=False, default='Win', max_length=255)
    profit = models.IntegerField(null=False, blank=False, default=0)
    image_link = models.URLField(null=False, blank=True, max_length=500)
    notes = models.CharField(null=False, blank=True, max_length=255)

    journal = models.ForeignKey('Journal', null=False, blank=False, on_delete=models.CASCADE, related_name='trade_journal')



