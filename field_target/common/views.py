
from django.views.generic import TemplateView


# Create your views here.
class ShowHomePageView(TemplateView):
    template_name = 'home.html'

class ShowCalculatorPageView(TemplateView):
    template_name = 'calculator.html'
