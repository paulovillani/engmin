from django.conf.urls import patterns, url
from planilha import views
from planilha.views import (PlanilhaView)

urlpatterns = patterns('',
	url(r'^/?$',  PlanilhaView.as_view(), name="Planilha"),
)