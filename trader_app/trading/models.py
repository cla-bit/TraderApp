from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

CustomUser = get_user_model()


class Trader(models.Model):
    trader = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Trader')
    slug = models.SlugField(unique=True, verbose_name='Slug Trader')
    amount = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Amount', null=True)

    class Meta:
        verbose_name = 'Trader'
        verbose_name_plural = 'Traders'
        indexes = [
            models.Index(fields=['trader', 'slug']),
            models.Index(fields=['amount']),
        ]

    def __str__(self):
        return self.trader.username

    def get_capital(self):
        return self.get_total_profit_loss() + self.amount

    def get_total_profit_loss(self):
        return sum(self.trades.values_list('profit_loss', flat=True))

    def get_absolute_url(self):
        return reverse('trading:user_dashboard', args=[self.slug])


class Trade(models.Model):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE, verbose_name='Trade', related_name='trades')
    balance = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Balance', null=True)
    profit_loss = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Profit/Loss', null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Trade'
        verbose_name_plural = 'Trades'
        indexes = [
            models.Index(fields=['trader', 'balance']),
            models.Index(fields=['trader', 'profit_loss']),
        ]

    def __str__(self):
        return f"Trader: {self.trader}\nAmount: {self.balance}\nProfit/Loss: {self.profit_loss}"

    def get_balance(self):
        return self.balance - self.profit_loss

