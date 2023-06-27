from django.shortcuts import render
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = "pages/index.html"

class about(TemplateView):
    template_name = "pages/about.html"