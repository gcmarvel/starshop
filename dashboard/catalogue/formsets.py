from oscar.apps.dashboard.catalogue import formsets as base_formsets
from django.core import exceptions

import random


class StockRecordFormSet(base_formsets.StockRecordFormSet):

    def set_initial_data(self):

        try:
            user_partner = self.user.partners.get()
        except (exceptions.ObjectDoesNotExist,
                exceptions.MultipleObjectsReturned):
            pass
        else:
            partner_field = self.forms[0].fields.get('partner', None)
            if partner_field and partner_field.initial is None:
                partner_field.initial = user_partner

        try:
            num_in_stock_field = self.forms[0].fields.get('num_in_stock', None)
            if num_in_stock_field and num_in_stock_field.initial is None:
                num_in_stock_field.initial = 1
        except Exception:
            pass

        try:
            partner_sku_field = self.forms[0].fields.get('partner_sku', None)
            if partner_sku_field and partner_sku_field.initial is None:
                partner_sku_field.initial = random.randint(0, 10000000)
        except Exception:
            pass
