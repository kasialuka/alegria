from django.shortcuts import render
from .models import Footer, Header
from django.views.generic import ListView, DetailView, TemplateView


# Create your views here.


class HeaderView(DetailView):
    model = Header




class FooterView(DetailView):

    model = Footer

    def get_footer(self):
        return self.model.name




