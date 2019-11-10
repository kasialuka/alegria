from django.shortcuts import render
from .models import Gallery
from django.views.generic import ListView, DetailView
from .models import Gallery


class GalleryListView(ListView):
    model = Gallery


class GalleryDetailView(ListView):
    model = Gallery

# Create your views here.

































































