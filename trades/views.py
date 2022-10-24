from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.detail import SingleObjectMixin

from . models import Journal


class HomeView(TemplateView):
    template_name = 'home.html'


class JournalListView(ListView):
    model = Journal
    template_name = 'journal_list.html'


class TradeView(DetailView):
    model = Journal
    template_name = 'trade_view.html'


class JournalCreateView(CreateView):
    model = Journal
    template_name = 'journal_create.html'
    fields = ['name']

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Journal added successfully.'
        )

        return super().form_valid(form)

class EditTradeView(SingleObjectMixin, FormView):

    model = Journal
    template_name = 'edit_trade.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Journal.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Journal.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return JournalTradesFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('trades:trade_view')
