from django.views.generic import ListView, DetailView, TemplateView
from .models import Food, FoodCategory
from  mainpage.models import  Footer, Header
from info.models import CompanyData
from meta.models import Meta

app_name = 'comida'


class FoodListView(ListView):

    model = Food


    def get_context_data(self, **kwargs):
        context = super(FoodListView, self).get_context_data(**kwargs)
        context['footer'] = CompanyData.objects.all().first()
        context['meta'] = Meta.objects.all().first()
        context['header'] = Header.objects.all().first()
        context['categories'] = FoodCategory.objects.all()
        return context


class FoodDetailView(DetailView):
    model = Food



    def get_context_data(self, **kwargs):
        context = super(FoodDetailView, self).get_context_data(**kwargs)
        context['footer'] = CompanyData.objects.all().first()
        return context


