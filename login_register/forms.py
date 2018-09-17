from django import forms

from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class MessageForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = PhoneNumberField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



    helper = FormHelper()
    helper.form_class = 'form-vertical'

    helper.layout = Layout(
        Field('first_name', placeholder="نام خود را وارد کنید"),
        Field('last_name', placeholder="نام خانوادگی تان را وارد کنید"),
        Field('phone_number', placeholder="شماره تلفن خود را وارد کنید"),
        Field('email', placeholder="ایمیل خود را وارد کنید"),

        AppendedText('password', '<a href=""><i class="fa fa-eye-slash" aria-hidden="true"></i></a>', placeholder="پسورد خود را  وارد نمایید", id="basic-addon1"),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-success"),
        )
    )
