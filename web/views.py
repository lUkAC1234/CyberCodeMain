from django.shortcuts import render
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = "pages/index.html"

class about(TemplateView):
    template_name = "pages/about.html"

class contact(TemplateView):
    template_name = "pages/contact.html"

class pricing(TemplateView):
    template_name = "pages/pricing.html"