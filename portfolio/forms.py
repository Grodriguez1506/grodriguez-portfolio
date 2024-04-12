from django import forms
from django.core import validators

class ContactForm(forms.Form):

    name = forms.CharField(
        label='Nombre y Apellido',
        max_length=40,
        validators=[validators.MinLengthValidator(6, 'El nombre y apellido es demasiado corto'),
                    validators.RegexValidator('^[A-Za-z ÁáÉéÍíÓóÚúñÑ]*$','El campo nombre tiene caracteres no permitidos')]
    )

    email = forms.CharField(
        label='Correo electrónico',
        validators=[validators.EmailValidator('Introduce un email válido')]
    )

    title = forms.CharField(
        label='Asunto',
        validators=[validators.MinLengthValidator(3, 'El asunto es demasiado corto')]
    )

    message = forms.CharField(
        label='Mensaje',
        widget= forms.Textarea(
            attrs={
                'placeholder':'Introduce tu mensaje'
            }
        )
    )