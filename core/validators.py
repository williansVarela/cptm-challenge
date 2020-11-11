import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

postal_code_re = re.compile(r'^\d{5}-\d{3}$')
phone_digits_re = re.compile(r'^\d{2}\-\d{4,5}\-\d{4}$')
cnpj_digits_re = re.compile(r'^(\d{2})[.-]?(\d{3})[.-]?(\d{3})/(\d{4})-(\d{2})$')
cpf_digits_re = re.compile(r'^(\d{3})\.?(\d{3})\.?(\d{3})\-?(\d{2})$')
cpfcnpj_digits_re = re.compile(r'(^(\d{3})\.?(\d{3})\.?(\d{3})\-?(\d{2})$)|(^(\d{2})\.?(\d{3})\.?(\d{3})\/?(\d{4})\-?(\d{2})$)')


INVALID_CPF = ("11111111111", "22222222222", "33333333333", "44444444444", "55555555555",
               "66666666666", "77777777777", "88888888888", "99999999999", "00000000000")


def digit_generator(cpf, weight):
    sum_digit = 0
    for n in range(weight - 1):
        sum_digit = sum_digit + int(cpf[n]) * weight
        weight = weight - 1

    digit = 11 - sum_digit % 11
    return 0 if digit > 9 else digit


def cpf_validator(value):
    # Extract numbers from string
    cpf = re.sub("[^0-9]", "", value)
    if len(cpf) != 11:
        raise ValidationError('CPF deve conter 11 números', 'invalid')

    # Calculate first validator digit from string
    first_digit = digit_generator(cpf, weight=10)

    # Calculate second validator digit from string
    second_digit = digit_generator(cpf, weight=11)

    # Checks whether the cpf is on the list of invalid persons or if a check digit does not match the digits calculated
    # in the expression
    if cpf in INVALID_CPF or (not cpf[-2:] == "%s%s" % (first_digit, second_digit)):
        raise ValidationError('Número de CPF inválido', 'invalid')


def cpfcnpj_validator(value):
    # Extract numbers from string
    cpf_cnpj = re.sub("[^0-9]", "", value)
    if len(cpf_cnpj) not in (11, 14):
        raise ValidationError('CPF deve conter 11 números e CNPJ 14 números', 'invalid')

    if not re.search(cpfcnpj_digits_re, cpf_cnpj):
        raise ValidationError('CPF ou CNPJ inválido', 'invalid')

    # Checks whether the cpf is on the list of invalid persons or if a check digit does not match the digits calculated
    # in the expression
    if cpf_cnpj in INVALID_CPF:
        raise ValidationError('Número de CPF inválido', 'invalid')

