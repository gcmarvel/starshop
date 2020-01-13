from django.conf.urls import url

from oscar.apps.catalogue.app import BaseCatalogueApplication as Application
from oscar.apps.catalogue.app import CatalogueApplication

from .views import ProductDetailView


class BaseCatalogueApplication(Application):

    def get_urls(self):
        urlpatterns = super(BaseCatalogueApplication, self).get_urls()
        urlpatterns += [
            url(r'^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail'),
            ]
        return self.post_process_urls(urlpatterns)


application = CatalogueApplication()
