from django.urls import reverse_lazy
from django.forms.formsets import formset_factory
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from oscar.apps.checkout.views import IndexView as CoreIndexView
from oscar.apps.checkout.views import PaymentMethodView as CorePaymentMethodView
from oscar.apps.checkout.views import PaymentDetailsView as CorePaymentDetailsView
from oscar.apps.checkout.session import CheckoutSessionMixin
from .forms import GatewayForm, NoMailForm, NameStarForm, MessageForm, AddressForm


class NoMaiView(CheckoutSessionMixin, FormView):

    template_name = 'checkout/nomail.html'
    form_class = NoMailForm
    success_url = reverse_lazy('checkout:name_star')

    def form_valid(self, form):
        phone = form.cleaned_data['phone']
        self.checkout_session.set_phone(phone)
        return super(NoMaiView).form_valid(form)


class IndexView(CoreIndexView):

    template_name = 'checkout/gateway.html'
    form_class = GatewayForm
    success_url = reverse_lazy('checkout:name_star')


class NameStarView(CheckoutSessionMixin, FormView):

    template_name = 'checkout/name_star.html'
    success_url = reverse_lazy('checkout:message')
    pre_conditions = ['check_basket_is_not_empty',
                      'check_basket_is_valid',
                      ]

    def get_form_class(self):
        return formset_factory(NameStarForm)

    def form_valid(self, form):
        star_names = {}
        i = 0
        for line in self.request.basket.all_lines():
            star_names['Звезда ' + line.product.title + '(' + str(line.product.id) + ')'] = self.request.POST['form-' + str(i) + '-name']
            i += 1
        self.checkout_session.set_star_names(star_names)
        return super(NameStarView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NameStarView, self).get_context_data(**kwargs)
        basket = self.request.basket.all_lines()
        form_class = formset_factory(NameStarForm)
        data = {'form-TOTAL_FORMS': self.request.basket.num_lines,
                'form-INITIAL_FORMS': '0',
                'form-MAX_NUM_FORMS': '',
                'form-MIN_NUM_FORMS': self.request.basket.num_lines,
                }
        formset = form_class(data)
        basket_and_formset = zip(basket, formset)
        context['basket_and_formset'] = basket_and_formset
        return context


class MessageView(CheckoutSessionMixin, FormView):

    template_name = 'checkout/message.html'
    success_url = reverse_lazy('checkout:shipping-address')
    pre_conditions = ['check_basket_is_not_empty',
                      'check_basket_is_valid',
                      ]

    def get_form_class(self):
        return formset_factory(MessageForm)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        return self.form_valid(form)

    def form_valid(self, form):
        messages = {}
        i = 0
        for line in self.request.basket.all_lines():
            publish = self.request.POST.get('form-' + str(i) + '-on_personal_page', False)
            if publish is not False:
                flag = 'Опубликовать'
            else:
                flag = 'НЕ ПУБЛИКОВАТЬ!'
            messages['Послание для звезды ' + line.product.title + '(' + str(line.product.id) + ')'] = self.request.POST['form-' + str(i) + '-message'] + ' ' + flag
            i += 1
        self.checkout_session.set_messages(messages)
        return super(MessageView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(MessageView, self).get_context_data(**kwargs)
        basket = self.request.basket.all_lines()
        form_class = formset_factory(MessageForm)
        data = {'form-TOTAL_FORMS': self.request.basket.num_lines,
                'form-INITIAL_FORMS': '0',
                'form-MAX_NUM_FORMS': '',
                'form-MIN_NUM_FORMS': self.request.basket.num_lines,
                }
        formset = form_class(data)
        names = self.checkout_session.get_star_names().values()
        basket_and_formset = zip(basket, formset, names)
        context['basket_and_formset'] = basket_and_formset
        return context


class ShippingAddressView(CheckoutSessionMixin, FormView):

    template_name = 'checkout/shipping_address.html'
    form_class = AddressForm
    success_url = reverse_lazy('checkout:payment-method')
    pre_conditions = ['check_basket_is_not_empty',
                      'check_basket_is_valid',
                      ]
    skip_conditions = ['skip_unless_basket_requires_shipping']

    def form_valid(self, form):
        address_fields = {'Фамилия': self.request.POST['surname'], 'Имя': self.request.POST['name'], 'Отчество': self.request.POST['second_name'],
                          'Адрес': self.request.POST['address'], 'Индекс': self.request.POST['postcode'], 'Телефон': self.request.POST['phone'],
                          'Комментарий': self.request.POST['comment']}
        self.checkout_session.set_address(address_fields)
        lines = []
        for line in self.request.basket.all_lines():
            lines_unit = []
            lines_unit.append(line.product.title)
            if line.product.product_class != 7:
                lines_unit.append(line.product.product_class)
                lines_unit.append(line.product.categories.all()[0])
            else:
                lines_unit.append(line.product.attr.starclass)
                lines_unit.append(line.product.attr.constellation)

            lines_unit.append(line.product.attr.magnitude)
            for price in line.get_price_breakdown():
                lines_unit.append(str(price[1]))
            lines.append(lines_unit)
        total = self.request.basket.total_excl_tax
        email = self.checkout_session.get_guest_email()
        phone = self.checkout_session.get_phone()
        address = self.checkout_session.get_address()
        if self.checkout_session.get_phone() is not None:
            template = f''' Заказ без почты!
            Телефон: {phone} 
    
            '''
        else:
            template = f''' E-mail: {email} 

                        '''
        zipped_template = zip(lines, self.checkout_session.get_star_names().values(), self.checkout_session.get_messages().values())
        for line, star_name, message in zipped_template:
            template += f'''
            ID звезды: {line[0]} 
                        
            Класс: {line[1]}, 
            
            Созвездие: {line[2]},
             
            Величина: {line[3]}
                        
            Цена: {line[4]} 
                        
            Имя звезды: {star_name}
                        
            Послание :{message}
            
                        '''
            template += f'''
            Всего: {total}
                    
            Адрес доставки:
                    '''
            for key, value in address.items():
                        template += f'''
            {key}: {value}
            '''

        subject = 'Оформлена покупка'
        message = template
        sender = 'no-reply@zvezdavpodarok.ru'
        recipients = ['starmaster@zvezdavpodarok.ru']
        send_mail(subject, message, sender, recipients)

        return super(ShippingAddressView, self).form_valid(form)


class PaymentMethodView(CorePaymentMethodView):

    pre_conditions = [
        'check_basket_is_not_empty',
        'check_basket_is_valid',
    ]


class PaymentDetailsView(CorePaymentDetailsView):

    pre_conditions = [
        'check_basket_is_not_empty',
        'check_basket_is_valid',
    ]
