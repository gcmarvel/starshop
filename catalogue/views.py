from oscar.apps.catalogue.views import ProductDetailView as OscarDetailView
from oscar.apps.catalogue.views import ProductCategoryView as OscarCategoryView


class ProductDetailView(OscarDetailView):

    def get_template_names(self):
        if self.template_name:
            return [self.template_name]

        return [
            '%s/detail-for-upc-%s.html' % (
                self.template_folder, self.object.upc),
            '%s/detail-for-class-%s.html' % (
                self.template_folder, self.object.get_product_class().slug),
            'detail.html']


class ProductCategoryView(OscarCategoryView):
    template_name = 'constellation.html'
