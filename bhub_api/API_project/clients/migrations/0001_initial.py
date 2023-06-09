# Generated by Django 4.1.7 on 2023-03-23 21:55

import clients.enums
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.IntegerField(blank=True, null=True, unique=True)),
                ('account', models.IntegerField(blank=True, null=True, unique=True)),
                ('bank_name', enumfields.fields.EnumField(enum=clients.enums.BanksName, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('declared_billing', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('addresses', models.CharField(max_length=255)),
                ('bank_accounts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='clients.accounts')),
            ],
        ),
    ]
