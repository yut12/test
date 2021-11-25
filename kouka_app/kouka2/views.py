from django.views import generic

from .forms import Kouka2Form

class Kouka2View(generic.TemplateView,generic.FormView):
    template_name = "base.html"
    form_class = Kouka2Form

# Create your views here.
