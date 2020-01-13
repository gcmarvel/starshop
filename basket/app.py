from django.conf.urls import url

from oscar.apps.basket.app import BasketApplication as Application

from .views import OneClickBuyView, ConstructView, RemoveFromBasket


class BasketApplication(Application):
    def get_urls(self):
        urlpatterns = super(BasketApplication, self).get_urls()
        urlpatterns += [
            url(r'^add/oneclickbuy/(?P<pk>\d+)/$', OneClickBuyView.as_view(), name='oneclickbuy'),
            url(r'^construct/$', ConstructView.as_view(), name='construct'),
            url(r'basket_remove/(?P<line>\d+)/$', RemoveFromBasket, name='removefrombasket')
        ]
        return self.post_process_urls(urlpatterns)


application = BasketApplication()
