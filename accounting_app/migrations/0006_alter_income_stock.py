# Generated by Django 4.2.5 on 2023-11-28 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_app', '0005_remove_invoice_print'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounting_app.stock', verbose_name='Склад'),
        ),
    ]