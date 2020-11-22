# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Line
import json


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'
    login_url = 'login/'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['page_title'] = 'Home'
        context['home_active'] = 'active'
        context['menu_navbar'] = 'core/menu_navbar.html'
        context['lines'] = Line.objects.all()
        context['occurrence_labels'] = json.dumps(["Rubi", "Diamante", "Esmeralda", "Turquesa", "Coral", "Safira", "Jade"])
        context['occurrence_data'] = json.dumps([10, 61, 27, 19, 4, 4, 2])
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['page_title'] = 'Dashboard'
        context['home_active'] = 'active'
        context['menu_navbar'] = 'core/menu_navbar.html'
        context['lines'] = Line.objects.all()
        context['occurrence_labels'] = json.dumps(["Rubi", "Diamante", "Esmeralda", "Turquesa", "Coral", "Safira", "Jade"])
        context['occurrence_data'] = json.dumps([10, 61, 27, 19, 4, 4, 2])
        context['current_line'] = self.kwargs['line'].capitalize()
        return context

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]



