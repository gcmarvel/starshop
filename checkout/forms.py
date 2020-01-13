from oscar.apps.checkout.forms import GatewayForm as CoreGatewayForm

from django import forms
from django.utils.translation import ugettext_lazy as _


class GatewayForm (CoreGatewayForm):
    username = forms.EmailField(label=_("My email address is"))
    GUEST = 'anonymous'
    CHOICES = (
        (GUEST, ('I am a new customer and want to checkout as a guest')),
    )
    options = forms.ChoiceField(widget=forms.widgets.RadioSelect,
                                choices=CHOICES, initial=GUEST)


class NoMailForm (forms.Form):
    phone = forms.CharField(max_length=20, label='Телефон', widget=forms.TextInput(attrs={'placeholder': '+71234567890'}))


class NameStarForm (forms.Form):
    name = forms.CharField(max_length=50, label='Имя звезды', widget=forms.TextInput(attrs={'placeholder': 'Например: Алина и Андрей'}))


class MessageForm (forms.Form):
    message = forms.CharField(max_length=3000, label='Послание', widget=forms.Textarea(attrs={'placeholder': 'Напишите,что бы Вы хотели сказать человеку, которому дарите звезду. При регистрации звезды с набором "Стандарт" или выше, мы отправим написанное Вами послание на состаренном свитке с сургучной печатью. В дополнение, по вашему желанию, '
                                                                                      'ваше послание может быть опубликовано на персональной странице приобретаемой звезды'}))
    on_personal_page = forms.BooleanField()


class AddressForm (forms.Form):
    surname = forms.CharField(max_length=30, label='Фамилия', widget=forms.TextInput(attrs={'placeholder': 'Например: Иванов'}), required=True)
    name = forms.CharField(max_length=30, label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Например: Иван'}), required=True)
    second_name = forms.CharField(max_length=30, label='Отчество', widget=forms.TextInput(attrs={'placeholder': 'Например: Иванович'}), required=False)
    address = forms.CharField(max_length=1000, label='Адрес', widget=forms.Textarea(attrs={'placeholder': 'Полный адрес доставки (страна, область, город, улица, дом, квартира)'}), required=True)
    postcode = forms.CharField(max_length=10, label='Индекс', widget=forms.TextInput(attrs={'placeholder': 'Например: 105043'}), required=True)
    phone = forms.CharField(max_length=20, label='Телефон', widget=forms.TextInput(attrs={'placeholder': 'Например: +71234567890'}), required=True)
    comment = forms.CharField(max_length=1000, label='Комментарий', widget=forms.Textarea(attrs={'placeholder': 'Комментарий к заказу'}), required=False)
