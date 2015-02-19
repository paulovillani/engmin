# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, FormView
from planilha.models import Composition
import itertools


# Create your views here.
class PlanilhaView(TemplateView):
	template_name = 'planilha.html'

	def get_context_data(self, **kwargs):
		context = super(PlanilhaView, self).get_context_data(**kwargs)
		context['compositions'] = Composition.objects.all()

		return context

class HomeView(TemplateView):
	template_name = 'home.html'

class RightMenuView(TemplateView):
	template_name = 'menu.right.html'