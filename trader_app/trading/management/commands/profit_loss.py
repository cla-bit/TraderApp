import decimal
import random
from django.core.management.base import BaseCommand
from trading.models import Trader, Trade
from django.utils import timezone


class Command(BaseCommand):
    help = 'Simulates profit and loss for each trade'

    def handle(self, *args, **options):
        traders = Trader.objects.all()

        for trader in traders:
            trader_amount = trader.amount
            for i in range(10):
                timestamp = timezone.now() - timezone.timedelta(days=i)
                percent_num = random.uniform(-0.1, 0.1)
                transaction_amt = int(trader_amount) * percent_num

                trader_amount += decimal.Decimal(transaction_amt)
            profit_loss = trader_amount - trader.amount
            # trade = Trade(trader=trader, amount=amount, profit_loss=profit_loss, timestamp=timestamp)
            trade = Trade.objects.create(trader=trader, balance=trader_amount, profit_loss=profit_loss, timestamp=timestamp)

            trade.save()

        self.stdout.write(self.style.SUCCESS('Done! Profit and Loss simulation completed'))


