from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Account


class AccountList(ListView):
    context_object_name = 'all_account'
    template_name = 'account_cbv/account_list.html'
    model = Account


class AccountCreate(CreateView):
    template_name = 'account_cbv/account_form.html'
    model = Account
    fields = ['title', 'email', 'username', 'name']
    success_url = reverse_lazy('account_cbv:account_list')


class AccountUpdate(UpdateView):
    template_name = 'account_cbv/account_form.html'
    model = Account
    fields = ['title', 'email', 'username', 'name']
    success_url = reverse_lazy('account_cbv:account_list')


class AccountDelete(DeleteView):
    template_name = 'account_cbv/account_delete.html'
    model = Account
    success_url = reverse_lazy('account_cbv:account_list')


class AccountDetail(ListView):
    template_name = 'account_cbv/account_detail.html'
    context_object_name = 'account_detail'


    def get_queryset(self):
        self.account = Account.objects.get(id=self.kwargs['pk'])
        return Account.objects.get(id=self.kwargs['pk'])




