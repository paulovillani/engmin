from django.conf.urls import patterns, url
from planilha import views
from planilha.views import (PlanilhaView, HomeView, RightMenuView)

urlpatterns = patterns('',
	url(r'^/?$',  HomeView.as_view(), name="Home"),
	url(r'^planilha.html?$',  PlanilhaView.as_view(), name="Planilha"),
	url(r'^menu.right.html?$',  RightMenuView.as_view(), name="MenuDireito"),	
)