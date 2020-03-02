from django.conf.urls import url

from oscar.apps.catalogue.app import CatalogueApplication as Application

from .views import ProductDetailView, ProductCategoryView


class CatalogueApplication(Application):

    def get_urls(self):
        urlpatterns = super(CatalogueApplication, self).get_urls()
        urlpatterns += [
            url(r'^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail'),
            url(r'^category/(?P<category_slug>[\w-]+(/[\w-]+)*)/$', ProductCategoryView.as_view(), name='constellation'),
            ]
        return self.post_process_urls(urlpatterns)


application = CatalogueApplication()
