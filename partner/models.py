from django.db import models

from oscar.apps.partner.abstract_models import AbstractStockRecord


class StockRecord(AbstractStockRecord):
    partner_sku = models.CharField("Складская запись", blank=True, null=True, max_length=128)

    class Meta:
        unique_together = None


from oscar.apps.partner.models import *  # noqa isort:skip