from django.db import models
from enumfields import EnumField

from .enums import BanksName


class Accounts(models.Model):
    agency = models.IntegerField(unique=True, blank=True, null=True)
    account = models.IntegerField(unique=True, blank=True, null=True)
    bank_name = EnumField(BanksName)

    def __str__(self):
        return (
            f"agency: {self.agency} - "
            f"account: {self.account} - "
            f"bank_name: {self.bank_name}"
        )


# Create your models here.
class Clients(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    declared_billing = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
    )
    addresses = models.CharField(max_length=255)
    bank_accounts = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, related_name="clients", db_index=True)

    def __str__(self):
        return (
            f"{self.pk} - "
            f"client: {self.company_name} - phone: {self.phone} - "
            f"bank_accounts: {self.bank_accounts}"
        )
