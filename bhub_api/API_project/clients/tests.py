import pytest

from clients.tests.factories.clients import ClientsFactory, AccountFactory

FAKE_NOW = datetime.datetime(2020, 5, 1, 14, 0, 32)

pytestmark = [pytest.mark.django_db]


class TestClients:
    @pytest.fixture
    def account(self):
        return AccountFactory.create()

    @pytest.fixture
    def client(self, account):
        return ClientsFactory.create(bank_accounts=account)

    def test_str_representation(self, client, account):
        expected_message = (
            f"{client.id} - "
            f"client: {client.company_name} - phone: {client.phone} - "
            f"bank_accounts: {client.bank_accounts}"
        )
        assert client.__str__() == expected_message

        expected_account = (
                f"agency: {client.pk} - "
                f"account: {client.account} - "
                f"bank_name: {client.bank_name}"
            )

        assert account.__str__() == expected_account
