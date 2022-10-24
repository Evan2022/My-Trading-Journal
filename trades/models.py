from django.db import models
from django.db import models


# Create your models here.
class Journal(models.Model):

    name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name


class Trade(models.Model):

    title = models.CharField(null=False, blank=False, max_length=255)

    journal = models.ForeignKey('Journal', null=False, blank=False, on_delete=models.CASCADE, related_name='trade_journal')

    