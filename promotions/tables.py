import django_tables2 as tables
from .models import Catalogue


class CatalogueTable(tables.Table):
    date = tables.DateColumn(format='d/m/Y', verbose_name='Дата регистрации')

    class Meta:
        model = Catalogue
        template_name = 'catalogue.html'
        fields = ('starid', 'name', 'country', 'magnitude', 'constellation', 'date')
        order_by = '-date'
