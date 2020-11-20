from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm, ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from django import forms
from core.utils import CustomErrorList
from core.models import User, Line
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['username'].widget.attrs = {'id': 'login', 'name': 'login'}
        self.fields['password'].widget.attrs = {'id': 'password', 'name': 'login'}


class UpdateProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].disabled = True

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('cpf', css_class='form-group col-md-2 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('date_of_birth', css_class='form-group col-md-2 mb-0'),
                Column('role', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Atualizar')
        )

    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Não é possível ver ou editar a senha deste usuário nesta página."
        ),
    )

    class Meta:
        model = User
        fields = ('name', 'cpf', 'email', 'date_of_birth', 'role')
        labels = {"date_of_birth": "Data Nasc."}


class UpdatePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs = {'id': 'id_old_password', 'class': 'form-control',
                                                    'placeholder': 'Digite a senha'}
        self.fields['new_password1'].widget.attrs = {'id': 'id_new_password1', 'class': 'form-control',
                                                     'placeholder': 'Digite a nova senha'}
        self.fields['new_password2'].widget.attrs = {'id': 'id_new_password2', 'class': 'form-control',
                                                     'placeholder': 'Confirme a nova senha'}

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('old_password', css_class='form-group col-md-4 mb-0'),
                Column('new_password1', css_class='form-group col-md-4 mb-0'),
                Column('new_password2', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar')
        )


class LineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-5 mb-0'),
                Column('humanized_name', css_class='form-group col-md-5 mb-0'),
                Column('number', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar')
        )

    class Meta:
        model = Line
        fields = '__all__'
        exclude = ('author',)