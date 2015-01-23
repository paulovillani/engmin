from django.contrib import admin
from planilha.models import Input, Composition, CompositionCoeficient

# Register your models here.

class InputAdmin(admin.ModelAdmin):
	list_display = ('code', 'description', 'unit', 'classification', 'unit_price')
admin.site.register(Input,InputAdmin)

class CompositionCoeficientInline(admin.TabularInline):
    model = CompositionCoeficient
    extra = 1

class CompositionAdmin(admin.ModelAdmin):
	list_display = ('code', 'description')
	inlines = (CompositionCoeficientInline,)
admin.site.register(Composition,CompositionAdmin)