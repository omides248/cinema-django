from django import forms

from django.utils.translation import ugettext_lazy as _

from phonenumber_field.formfields import PhoneNumberField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class RegisterForm(forms.Form):

    first_name = forms.CharField(label=_('first name'))
    last_name = forms.CharField(label=_('last name'))
    phone_number = PhoneNumberField(label=_('phone_number'))
    email = forms.EmailField(label=_('email'))
    password = forms.CharField(widget=forms.PasswordInput, label=_('password'))
    password_reapet = forms.CharField(widget=forms.PasswordInput, label=_('password_reapet'))



    helper = FormHelper()
    helper.form_class = 'form-vertical'

    helper.layout = Layout(
        Field('first_name', placeholder=_("Enter your first name")),
        Field('last_name', placeholder=_("Enter your last name")),
        Field('phone_number', placeholder=_("Enter your phone number")),
        Field('email', placeholder=_("Enter your email address")),

        AppendedText('password', '<a href=""><i class="fa fa-eye-slash" aria-hidden="true"></i></a>', placeholder=_("Enter your password"), id="basic-addon1"),
        AppendedText('password_reapet', '<a href=""><i class="fa fa-eye-slash" aria-hidden="true"></i></a>', placeholder=_("Enter your repeat password"), id="basic-addon1"),
        FormActions(
            Submit('register_form', _('Register'), css_class="btn-info"),style="margin: auto; width: -moz-fit-content;"
        )
    )




class LoginForm(forms.Form):

    email = forms.EmailField(label=_('email'))
    password = forms.CharField(widget=forms.PasswordInput, label=_('password'))
    checkbox_remember = forms.BooleanField(label=_('checkbox remember'), required = False, initial=True)

    helper = FormHelper()
    helper.form_class = 'form-vertical'

    helper.layout = Layout(
        Field('email', placeholder=_("Enter your email address")),

        AppendedText('password', '<a href=""><i class="fa fa-eye-slash" aria-hidden="true"></i></a>', placeholder=_('Enter your password')),

        Field('checkbox_remember'),
# margin: auto;text-align: center;width: 50%;
        FormActions(
        Submit('login_form', _("Login"), css_class="btn-success"), style="margin: auto; width: -moz-fit-content;"
        ),
        HTML("""<p id="title-forget-password"><a href="#" id="forget-password">فراموشی رمز عبور</a></p>"""),
    )
