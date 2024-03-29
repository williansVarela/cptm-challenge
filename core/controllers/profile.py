# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from core.forms import UpdateProfileForm, UpdatePasswordForm
from core.models import User


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'core/base_crispy_form.html'
    form_class = UpdateProfileForm
    model = User
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        context['menu_navbar'] = 'core/menu_navbar_empty.html'
        context['page_title'] = 'Perfil'
        context['form_title'] = 'Perfil'
        context['back_button'] = 'Voltar'
        context['back_link'] = reverse_lazy('home')
        return context

    def get_object(self, queryset=None):
        """This loads the profile of the currently logged in user"""
        return User.objects.get(email=self.request.user)

    def form_valid(self, form):
        """Here is where you set the user for the new profile"""
        instance = form.instance  # This is the new object being saved
        instance.user = self.request.user
        instance.save()

        if form.is_valid():
            messages.success(self.request, 'Seus dados foram atualizado com sucesso!', extra_tags='alert alert-success')
        else:
            messages.error(self.request, 'Por favor corrija o erro acima.', extra_tags='alert alert-danger')

        return super(UpdateProfileView, self).form_valid(form)


class PasswordResetByUser(PasswordChangeView):
    template_name = 'core/base_crispy_form.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('change_password')

    def get_context_data(self, **kwargs):
        context = super(PasswordResetByUser, self).get_context_data(**kwargs)
        context['menu_navbar'] = 'core/menu_navbar_empty.html'
        context['page'] = 'Perfil'
        context['page_title'] = 'Alterar Senha'
        context['form_title'] = 'Atualizar Senha'
        context['back_button'] = 'Voltar'
        context['back_link'] = reverse_lazy('home')
        return context

    def form_valid(self, form):
        if form.is_valid():
            messages.success(self.request, 'Sua senha foi atualizada com sucesso!', extra_tags='alert alert-success')
        else:
            messages.error(self.request, 'Por favor corrija o(s) erro(s) acima.', extra_tags='alert alert-danger')

        return super(PasswordResetByUser, self).form_valid(form)


