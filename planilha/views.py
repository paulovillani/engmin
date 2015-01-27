# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, FormView
from planilha.models import Composition

# Create your views here.
class PlanilhaView(TemplateView):
	template_name = 'planilha.html'

	def get_context_data(self, **kwargs):
		context = super(PlanilhaView, self).get_context_data(**kwargs)
		context['compositions'] = Composition.objects.all()

		return context