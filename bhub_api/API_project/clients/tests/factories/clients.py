
import factory
from clients.enums import BanksName
from clients.models import Accounts, Clients


class AccountsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BanksName

    agency = 36102
    account = 534765
    bank_name = BanksName.INVALID


class ClientsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Clients

    company_name = "Bhub"
    phone = "992224988"
    declared_billing = 20000.50
    addresses = 'Rua Cantor Luiz Gonzaga 75, apto 302'
    bank_accounts = factory.SubFactory(AccountsFactory)