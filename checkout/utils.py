from oscar.apps.checkout.utils import CheckoutSessionData as CoreCheckoutSessionData


class CheckoutSessionData(CoreCheckoutSessionData):

    def set_phone(self, phone):
        self._set('guest', 'phone', phone)

    def get_phone(self):
        return self._get('guest', 'phone')

    def set_star_names(self, names):
        self._set('names', 'star_names', names)

    def get_star_names(self):
        return self._get('names', 'star_names',)

    def set_messages(self, messages):
        self._set('messages', 'star_messages', messages)

    def get_messages(self):
        return self._get('messages', 'star_messages')

    def set_address(self, address):
        self._set('address', 'new_address', address)

    def get_address(self):
        return self._get('address', 'new_address')
