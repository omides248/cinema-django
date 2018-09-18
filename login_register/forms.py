from django import forms

from django.utils.translation import ugettext_lazy as _

from phonenumber_field.formfields import PhoneNumberField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class RegisterForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = PhoneNumberField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



    helper = FormHelper()
    helper.form_class = 'form-vertical'

    helper.layout = Layout(
        Field('first_name', placeholder=_("firstName_RegisterForm_placeholder")),
        Field('last_name', placeholder=_("lastName_RegisterForm_placehodler")),
        Field('phone_number', placeholder=_("phoneNumber_RegisterForm_placehodler")),
        Field('email', placeholder=_("email_RegisterForm_placeholder")),

        AppendedText('password', '<a href=""><i class="fa fa-eye-slash" aria-hidden="true"></i></a>', placeholder=_("password_RegisterForm_placeholder"), id="basic-addon1"),
        AppendedText('password', '<a href=""><i class="fa fa-eye-slash" aria-hidden="true"></i></a>', placeholder=_("password_RegisterForm_placeholder"), id="basic-addon1"),
        FormActions(
            Submit('register_form', _('Register'), css_class="btn-success"),
        )
    )




class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    helper = FormHelper()
    helper.form_class = 'form-vertical'

    helper.layout = Layout(
        Field('email'),

        AppendedText('password', '<a href=""><i class="fa fa-eye-slash" aria-hidden="true"></i></a>'),

        FormActions(
        Submit('login_form', _("Login"), css_class="btn-success")
        )
    )
