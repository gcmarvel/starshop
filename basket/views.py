from oscar.apps.basket.views import BasketAddView as CoreBasketView
from oscar.apps.basket.models import Line as BasketLine

from django.shortcuts import redirect
from django.views.generic import View
from catalogue.models import Product
from oscar.apps.partner.models import StockRecord

from oscar.apps.catalogue.models import ProductCategory
import random
import datetime

from oscar.core.loading import get_class, get_classes
from django.utils.http import is_safe_url
from django.shortcuts import resolve_url

OrderTotalCalculator = get_class(
    'checkout.calculators', 'OrderTotalCalculator')
BasketLineFormSet, SavedLineFormSet = get_classes(
    'basket.formsets', ('BasketLineFormSet', 'SavedLineFormSet'))


class OneClickBuyView(CoreBasketView):

    def get_success_url(self):
        post_url = self.request.POST.get('next')
        if post_url and is_safe_url(post_url, self.request.get_host()):
            return post_url
        return resolve_url('basket:summary')


class ConstructView(View):

    def post(self, request):
        constellation = request.POST.get('constellation-select')
        star_class = request.POST.get('starclass-select')
        magnitude = request.POST.get('present-select')
        date = datetime.datetime.now()
        randomslug = random.randint(1, 1000000)
        randomsku = random.randint(1, 1000000)
        new_product = Product(structure='standalone', title=f'{star_class} в созвездии {constellation}', slug=f'constructor_{randomslug}',
                              date_created=f'{date}', date_updated=f'{date}', is_discountable='0', product_class_id='7')

        if magnitude == 'Девятая звёздная величина':
            price = 3000
            new_product.attr.magnitude = 9

        elif magnitude == 'Восьмая звёздная величина':
            price = 5990
            new_product.attr.magnitude = 8

        elif magnitude == 'Седьмая звёздная величина':
            price = 11900
            new_product.attr.magnitude = 7

        elif magnitude == 'Шестая звёздная величина':
            price = 19500
            new_product.attr.magnitude = 6

        elif magnitude == 'Пятая звёздная величина':
            price = 32000
            new_product.attr.magnitude = 5

        new_product.currency = '₽'
        new_product.attr.starclass = star_class
        new_product.attr.constellation = constellation
        new_product.save()
        new_prodcat = ProductCategory(product_id=new_product.id, category_id='25')
        new_prodcat.save()
        new_stockrecord = StockRecord(partner_sku=f'constructor_{randomsku}', price_excl_tax=f'{price}', num_in_stock='1',
                                      date_created=f'{date}', date_updated=f'{date}', partner_id='1', product_id=new_product.id, price_currency='₽')
        new_stockrecord.save()

        basket = request.basket
        basket.add_product(new_product, 1)

        return redirect('basket:summary')


def RemoveFromBasket(request, line):
    d_line = BasketLine.objects.filter(id=line)
    d_line.delete()
    request.basket.save()
    return redirect('basket:summary')



