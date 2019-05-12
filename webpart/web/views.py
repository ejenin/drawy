from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Create your views here.
#def index(request):
    #return HttpResponse("Hello, world!")