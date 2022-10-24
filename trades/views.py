from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView)
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

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



