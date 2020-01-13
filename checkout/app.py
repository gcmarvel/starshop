from django.conf.urls import url

from oscar.apps.checkout.app import CheckoutApplication as Application

from .views import IndexView, NoMaiView, NameStarView, MessageView


class CheckoutApplication(Application):
    def get_urls(self):
        urlpatterns = super(CheckoutApplication, self).get_urls()
        urlpatterns += [
            url(r'^$', IndexView.as_view(), name='index'),
            url(r'nomail/$', NoMaiView.as_view(), name='nomail'),
            url(r'name-star/$', NameStarView.as_view(), name='name_star'),
            url(r'message/$', MessageView.as_view(), name='message'),
        ]
        return self.post_process_urls(urlpatterns)


application = CheckoutApplication()

