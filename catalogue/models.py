from oscar.apps.catalogue.abstract_models import AbstractProduct

from oscar.models.fields import NullCharField


class Product(AbstractProduct):
    upc = NullCharField("UPC", max_length=64, blank=True, null=True, unique=False,)

    def linktocategory(self):
        prc = ProductCategory.objects.get(product_id=self.id)
        cat = Category.objects.get(id=prc.category_id)
        return cat.name


from oscar.apps.catalogue.models import *
