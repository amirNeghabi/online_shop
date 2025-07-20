from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'homepage.html'


class AboutUsPageView(TemplateView):
    template_name = 'pages/about_us.html'
