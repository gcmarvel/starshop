from oscar.apps.catalogue.views import ProductDetailView as OscarDetailView


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

