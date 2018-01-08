from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy




def home(request):
    html = """
    <p>welcome</p>
    """
    return HttpResponse(html)