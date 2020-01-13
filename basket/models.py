from oscar.apps.basket.abstract_models import AbstractBasket
from oscar.core.loading import get_class, get_model

LineOfferConsumer = get_class('basket.utils', 'LineOfferConsumer')


class Basket(AbstractBasket):

    def is_shipping_required(self):
        for line in self.all_lines():
            if line.stockrecord.price_excl_tax != 3000:
                return True
        return False

from oscar.apps.basket.models import *
