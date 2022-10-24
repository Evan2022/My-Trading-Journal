from django.shortcuts import render
from django.views.generic import (TemplateView, ListView)
from django.urls import reverse
from django.http import HttpResponseRedirect

from . models import Journal


class HomeView(TemplateView):
    template_name = 'home.html'


class JournalsListView(ListView):
    model = Journal
    template_name = 'journal_list.html'