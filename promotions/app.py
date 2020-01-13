from django.conf.urls import url

from oscar.apps.promotions.app import PromotionsApplication as Application

from .views import Reviews, Terms, Oferta, Agreement, SendStoryThanksView


class PromotionsApplication(Application):

    def get_urls(self):
        urlpatterns = super(PromotionsApplication, self).get_urls()
        urlpatterns += [
            url(r'^reviews/$', Reviews.as_view(), name='reviews'),
            url(r'^terms/$', Terms.as_view(), name='terms'),
            url(r'sendstory-thanks/$', SendStoryThanksView.as_view(), name='sendstory-thanks'),
            url(r'^oferta/$', Oferta.as_view(), name='oferta'),
            url(r'^agreement/$', Agreement.as_view(), name='agreement'),
        ]
        return self.post_process_urls(urlpatterns)


application = PromotionsApplication()
