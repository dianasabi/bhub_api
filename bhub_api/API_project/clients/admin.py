from django.contrib import admin


# Register your models here.
from .models import Clients, Accounts


class AccountsAdmin(admin.ModelAdmin):
    list_display = (
        "agency",
        "account",
        "bank_name"
    )
    list_filter = ["id"]


class ClientsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_time",
        "company_name",
        "phone",
        "declared_billing",
        "addresses",
        "bank_accounts"
    )
    list_filter = ["id"]


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Accounts, AccountsAdmin)
