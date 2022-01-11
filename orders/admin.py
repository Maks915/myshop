from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'Имя', 'Фамилия', 'email',
                    'Адрес', 'Почтовый_индекс', 'Город', 'Оплачен',
                    'created', 'updated']
    list_filter = ['Оплачен', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)