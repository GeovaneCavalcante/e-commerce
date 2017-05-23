from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Menssagem', widget=forms.Textarea)

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome: {0}\nEmail: {1}\nMenssagem: {2}\n'.format(name, email, message)
        send_mail(
            'Contato do django ecommerce',
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['geovanefeitosacavalcante@gmail.com', ]
        )