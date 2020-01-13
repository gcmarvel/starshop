from django import forms


class SendStoryForm (forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Мой адрес электронной почты'}))
    story = forms.Field(widget=forms.Textarea(attrs={'placeholder': 'История...'}))
