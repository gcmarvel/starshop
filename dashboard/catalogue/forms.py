from oscar.apps.dashboard.catalogue import forms as base_forms
from django import forms
from oscar.core.loading import get_model
from django.utils.translation import ugettext_lazy as _

Product = get_model('catalogue', 'Product')
StockRecord = get_model('partner', 'StockRecord')


class ProductForm(base_forms.ProductForm):

    class Meta:
        model = Product
        fields = [
            'title', 'is_discountable', 'structure']
        widgets = {
            'structure': forms.HiddenInput()
        }


class StockRecordForm(base_forms.StockRecordForm):

    class Meta:
        model = StockRecord
        fields = ['id',
            'price_excl_tax',
            'num_in_stock',
        ]


class ProductSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255, required=False, label=_('Product title'))

    def clean(self):
        cleaned_data = super(ProductSearchForm, self).clean()
        cleaned_data['title'] = cleaned_data['title'].strip()
        return cleaned_data

