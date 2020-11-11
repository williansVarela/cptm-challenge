from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core.utils import CustomErrorList
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['username'].widget.attrs = {'id': 'login', 'name': 'login'}
        self.fields['password'].widget.attrs = {'id': 'password', 'name': 'login'}
