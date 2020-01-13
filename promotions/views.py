from .models import Catalogue, CatalogueFilter
from .tables import CatalogueTable
from .tabledata import new_data
from .tabledata import new_reviews
from .forms import SendStoryForm

from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.mail import send_mail


class HomeView(SingleTableMixin, FilterView, FormView):
    template_name = 'index.html'
    model = Catalogue
    table_class = CatalogueTable
    table_data = new_data
    form_class = SendStoryForm
    success_url = 'sendstory-thanks'

    filterset_class = CatalogueFilter

    table_pagination = {
        'per_page': 8
    }

    def get_queryset(self):
        qs = self.request.GET.get('starid')
        data_list = new_data

        def generate_data(qs, data_list):
            global newest_data
            newest_data = [x for x in data_list if x['starid'] == str(qs)]
            return newest_data

        generate_data(qs, data_list)

    def get_table_data(self):
        if newest_data == []:
            return new_data
        else:
            return newest_data

    def form_valid(self, form):
        email = form.cleaned_data['email']
        story = form.cleaned_data['story']

        template = f''' Email: {email} 
                        История: {story}
        '''
        subject = 'Прислана история покупки'
        message = template
        sender = 'Звезда в Подарок'
        recipients = ['zvezdavpodaroktest@gmail.com']
        send_mail(subject, message, sender, recipients)

        return super().form_valid(form)


class SendStoryThanksView(TemplateView):
    template_name = 'sendstory-thanks.html'


class Reviews(TemplateView):
    template_name = 'reviews.html'

    def get_context_data(self, *args, **kwargs):
        reviews_list = sorted(new_reviews, key=lambda i: i['date'], reverse=True)
        context = super(Reviews, self).get_context_data(*args, **kwargs)
        context['reviews'] = reviews_list
        return context


class Terms(TemplateView):
    template_name = 'terms.html'


class Oferta(TemplateView):
    template_name = 'oferta.html'


class Agreement(TemplateView):
    template_name = 'agreement.html'
