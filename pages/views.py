from django.http import HttpResponse
from django.views.generic import TemplateView


def homePageView(request):
    return HttpResponse("Hola mundo!")



class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
