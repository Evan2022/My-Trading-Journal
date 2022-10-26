from django.forms.models import inlineformset_factory

from .models import Journal, Trade

JournalTradesFormset = inlineformset_factory(Journal, Trade, fields=('strategy', 'balance', 'win_or_loss', 'profit', 'image_link', 'notes',))