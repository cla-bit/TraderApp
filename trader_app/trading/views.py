from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.utils import timezone
from .forms import TraderCreationForm, TraderLoginForm
from .models import Trader, Trade

# Create your views here.


def trader_sign_up(request):
    context = {}
    if request.method == 'POST':
        trader_form = TraderCreationForm(request.POST)
        if trader_form.is_valid():
            new_trader = trader_form.save()

            trader_new = Trader.objects.create(trader=new_trader, slug=new_trader.username, amount=100)
            trader_new.save()
            login(request, new_trader)
            return redirect('trading:user_dashboard', slug=trader_new.slug)
        else:
            context['trader_form'] = trader_form
            return render(request, 'trader_sign_up.html', context)
    else:
        trader_form = TraderCreationForm()
        context['trader_form'] = trader_form
        return render(request, 'trader_sign_up.html', context)


def trader_sign_in(request):
    context = {}
    if request.method == 'POST':
        trader_form = TraderLoginForm(request, data=request.POST)
        if trader_form.is_valid():
            trader = trader_form.get_user()

            if trader is not None:
                login(request, trader)
                if trader.is_superuser:
                    return redirect('trading:admin_dashboard')
                return redirect('trading:user_dashboard', slug=trader.trader.slug)
        else:
            context['trader_form'] = trader_form
            return render(request, 'trader_sign_in.html', context)
    else:
        trader_form = TraderLoginForm()
        context['trader_form'] = trader_form
        return render(request, 'trader_sign_in.html', context)


def trader_logout(request):
    logout(request)
    return redirect('trading:trader_sign_in')


@login_required(login_url='trading:trader_sign_in')
def user_dashboard(request, slug=None):
    context = {}
    trader = get_object_or_404(Trader, slug=slug)
    capital = trader.get_capital()
    trades = Trade.objects.filter(trader=trader)
    balance = sum(trade.get_balance() for trade in trades)
    time = max(trade.timestamp for trade in trades)

    profit_loss = trader.get_total_profit_loss()

    context['trader'] = trader
    context['capital'] = capital
    context['trades'] = trades
    context['balance'] = balance
    context['profit_loss'] = profit_loss
    context['time'] = time
    return render(request, 'user_dashboard.html', context)


@login_required(login_url='trading:trader_sign_in')
@user_passes_test(lambda u: u.is_superuser, login_url='trading:trader_sign_in')
def admin_dashboard(request):
    context = {}
    traders = Trader.objects.all()
    admin_name = request.user.username
    trades = Trade.objects.aggregate(total_trades=Count('id'))['total_trades']
    total_balance = traders.aggregate(Sum('trades__balance'))['trades__balance__sum']
    amount = traders.aggregate(Sum('amount'))['amount__sum']
    profit_loss = traders.aggregate(Sum('trades__profit_loss'))['trades__profit_loss__sum']
    time = timezone.now()

    context['time'] = time
    context['traders'] = traders
    context['trades'] = trades
    context['admin'] = admin_name
    context['total_balance'] = total_balance
    context['amount'] = amount
    context['profit_loss'] = profit_loss
    return render(request, 'admin_dashboard.html', context)

