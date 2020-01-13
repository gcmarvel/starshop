from oscar.apps.promotions.models import *

from django.db import models
import django_filters


class Catalogue(models.Model):
    starid = models.CharField(max_length=100, verbose_name='ID Звезды')
    name = models.CharField(max_length=100, verbose_name='Владелец')
    country = models.CharField(max_length=100, verbose_name='Страна')
    magnitude = models.FloatField(verbose_name='Звездная величина')
    constellation = models.CharField(max_length=100, verbose_name='Созвездие')
    date = models.DateField()

class CatalogueFilter(django_filters.FilterSet):
    starid = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Catalogue
        fields = ['starid']
