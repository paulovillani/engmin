# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
CLAS_CHOICES = [
    ['MOD', u'Mão de Obra'],
    ['SER', u'Serviço'],
    ['MAT', 'Material'],
    ['EQH', 'Equipamento'],
    ['EQI', 'Equipamento2']
]

UNIT_CHOICES = [
	['h', 'h'],
	['m', 'm'],
	['m2', 'm²'],
	['m3', 'm³'],
	['un', 'Un'],
	['kg', 'kg']
]

class Input(models.Model):
	class Meta:
		verbose_name = u"Insumo"
		verbose_name_plural = u"Insumos"
	code = models.CharField(max_length=32, primary_key=True, verbose_name=u"Código")
	description = models.CharField(max_length=512, verbose_name=u"Descrição")
	unit = models.CharField(max_length=8, choices=UNIT_CHOICES, verbose_name=u"Unidade")
	classification = models.CharField(max_length=3, choices=CLAS_CHOICES, 
									  verbose_name=u"Classificação")
	unit_price  = models.FloatField(verbose_name=u"Preço unitário")

	def __unicode__(self):
		return self.code

class Composition(models.Model):
	class Meta:
		verbose_name = u"Composição"

	code = models.CharField(max_length=32, primary_key=True, verbose_name=u"Código")
	description = models.CharField(max_length=512, verbose_name=u"Descrição")
	unit = models.CharField(max_length=8, choices=UNIT_CHOICES, verbose_name=u"Unidade")
	inputs = models.ManyToManyField(Input, through='CompositionCoeficient', verbose_name=u"Insumos")

	def __unicode__(self):
		return self.description

	@property
	def mod_price(self):
		mod_coef = CompositionCoeficient.objects.filter(composition=self, inputs__classification="MOD")
		mod = 0
		for coef in mod_coef:
			mod += coef.total_price;
		return mod

	@property
	def others_price(self):
		others_coef = CompositionCoeficient.objects.filter(composition=self).exclude(inputs__classification = "MOD")
		others = 0
		for coef in others_coef:
			others += coef.total_price;
		return others




class CompositionCoeficient(models.Model):
	class Meta:
		verbose_name = u"Coeficiente da composição"
		verbose_name_plural = u"Coeficientes da composição"
		unique_together = ("inputs", "composition")

	inputs = models.ForeignKey(Input)
	composition = models.ForeignKey(Composition)
	coeficient = models.FloatField(verbose_name=u"Coeficiente")

	@property
	def total_price(self):
		return self.coeficient*self.inputs.unit_price
