from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.views.generic import ListView
from threading import Thread
from multiprocessing import Process
from datetime import datetime

from banks.banks_registration.tinkoff import (get_all_tinkoff,
                                              get_all_tinkoff_exchanges,
                                              get_tinkoff_not_looped,
                                              )
from banks.banks_registration.wise import get_all_wise_exchanges, get_wise_not_looped
from banks.models import BanksExchangeRates, Banks, IntraBanksNotLoopedExchanges, BankInvestExchanges
from core.intra_exchanges import BestBankIntraExchanges

from banks.multithreading import all_banks_exchanges
from banks.banks_config import BANKS_CONFIG

from banks.currency_markets_registration.tinkoff_invest import get_tinkoff_invest_exchanges


def banks(request):
    template = 'banks/banks.html'
    return render(request, template)


class BanksRatesList(ListView):

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BanksRatesList, self).get_context_data(**kwargs)
        context['bank_names'] = list(BANKS_CONFIG.keys())
        context['bank_rates'] = self.get_queryset()
        context['last_update'] = self.get_queryset().latest(
            'update').update.updated
        return context


class BankRatesList(ListView):

    def get_bank_name(self):
        return self.kwargs.get('bank_name').capitalize()

    def get_queryset(self):
        bank = Banks.objects.get(name=self.get_bank_name())
        return self.model.objects.filter(bank=bank)

    def get_context_data(self, **kwargs):
        context = super(BankRatesList, self).get_context_data(**kwargs)
        context['bank_names'] = list(BANKS_CONFIG.keys())
        context['bank_rates'] = self.get_queryset()
        context['bank_name'] = self.get_bank_name()
        context['last_update'] = self.get_queryset().latest(
            'update').update.updated
        return context


class BankInternalExchange(BankRatesList):
    model = BanksExchangeRates
    template_name = 'banks/internal_exchange.html'


class BanksInternalExchange(BanksRatesList):
    model = BanksExchangeRates
    template_name = 'banks/internal_exchange.html'


class BankInternalTripleExchange(BankRatesList):
    model = IntraBanksNotLoopedExchanges
    template_name = 'banks/internal_triple_exchange.html'


class BanksInternalTripleExchange(BanksRatesList):
    model = IntraBanksNotLoopedExchanges
    template_name = 'banks/internal_triple_exchange.html'


class BankInvestExchange(ListView):
    template_name = 'banks/currency_market_exchanges.html'

    def get_queryset(self):
        currency_markets_name = BANKS_CONFIG[self.kwargs.get('bank_name').capitalize()]['bank_invest_exchanges']
        get_list_or_404(
            BankInvestExchanges,
            currency_market__name__in=currency_markets_name
        )

    def get_context_data(self, **kwargs):
        context = super(BankInvestExchange, self).get_context_data(**kwargs)
        context['bank_names'] = list(BANKS_CONFIG.keys())
        context['bank_name'] = self.kwargs.get('bank_name').capitalize()
        return context


class BanksInvestExchange(ListView):
    template_name = 'banks/currency_market_exchanges.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(BanksInvestExchange, self).get_context_data(**kwargs)
        context['bank_names'] = list(BANKS_CONFIG.keys())
        return context


def tinkoff_not_looped(request):
    return get_tinkoff_not_looped()


def wise_not_looped(request):
    return get_wise_not_looped()


def tinkoff(request):
    return get_all_tinkoff_exchanges()


def tinkoff_all(request):
    return get_all_tinkoff()


def tinkoff_invest_exchanges(request):
    return get_tinkoff_invest_exchanges()


def wise(request):
    return get_all_wise_exchanges()


def best_bank_intra_exchanges(request):
    get_best_bank_intra_exchanges = BestBankIntraExchanges()
    return get_best_bank_intra_exchanges.main()


def get_all_banks_exchanges(request):
    all_banks_exchanges()
