from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy




def home(request):
    html = """
    <p>welcome</p>
    <a href={% url 'account_cbv: account_list' %}>for proceding cbv by pk</a>
    <a href={% url 'account_slug: account_list' %}>for proceding cbv by slug</a>
    """
    return HttpResponse(html)

