from django.db import models
from core.validators import cpf_validator, cpfcnpj_validator
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import uuid


class CPFField(models.CharField):
    default_validators = [cpf_validator]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 11)
        super().__init__(*args, **kwargs)


class CPFCNPJField(models.CharField):
    default_validators = [cpfcnpj_validator]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 14)
        super().__init__(*args, **kwargs)


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def create_user(self, name, email, cpf, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            cpf=cpf,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, cpf,  date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            name=name,
            email=email,
            cpf=cpf,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    username = None
    name = models.CharField(max_length=100, verbose_name='Nome Completo')
    cpf = CPFField(null=True, verbose_name='CPF')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Endereço de e-mail')
    date_of_birth = models.DateField(null=True, verbose_name='Data de Nascimento')
    role = models.CharField(max_length=100, blank=True, null=True, verbose_name='Função')
    is_active = models.BooleanField(default=True, verbose_name='Perfil Ativo')
    is_admin = models.BooleanField(default=False, verbose_name='Administrador')
    is_staff = models.BooleanField(default=False, verbose_name='Equipe')
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cpf', 'date_of_birth']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_first_name(self):
        return self.name.split()[0].title()

    def get_last_name(self):
        return self.name.split()[-1].title()

    def get_first_last(self):
        name_split = self.name.split()
        return f"{name_split[0].title()} {name_split[-1].title()}"

    def get_short_name(self):
        name_split = self.name.split()
        return name_split[0][0] + name_split[-1][0]

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        app_label = 'core'
        permissions = (("admin_user", "Can Admin Usuários"),
                       ("disable_user", "Can disable Usuário"),)


class Line(models.Model):
    name = models.CharField(max_length=30, null=True, verbose_name='Nome')
    humanized_name = models.CharField(max_length=30, null=True, verbose_name='Nome Humanizado')
    number = models.IntegerField(null=True, verbose_name='Número')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name='Criador')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.humanized_name

    class Meta:
        verbose_name = 'Linha'
        verbose_name_plural = 'Linhas'
        app_label = 'core'