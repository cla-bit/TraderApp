from django.contrib import admin
from .models import Trader, Trade

# Register your models here.


@admin.register(Trader)
class TraderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('trader',)}
    list_display = ['trader', 'amount', 'get_total_profit_loss', 'get_capital']
    list_filter = ['trader']
    search_fields = ['trader']


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ['trader', 'balance', 'profit_loss', 'get_balance', 'timestamp']