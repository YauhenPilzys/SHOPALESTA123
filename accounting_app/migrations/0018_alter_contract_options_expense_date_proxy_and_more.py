# Generated by Django 4.2.5 on 2023-10-12 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_app', '0017_contract'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Договор', 'verbose_name_plural': 'Договора'},
        ),
        migrations.AddField(
            model_name='expense',
            name='date_proxy',
            field=models.DateField(blank=True, null=True, verbose_name='Дата доверенности'),
        ),
        migrations.AddField(
            model_name='expense',
            name='number_proxy',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер доверенности'),
        ),
        migrations.AddField(
            model_name='expense',
            name='proxy_user',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Кем выдана довереннось'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_app.client', verbose_name='Клиент'),
        ),
    ]