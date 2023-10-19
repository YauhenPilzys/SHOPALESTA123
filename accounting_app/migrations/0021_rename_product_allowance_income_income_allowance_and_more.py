# Generated by Django 4.2.5 on 2023-10-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_app', '0020_stock_product_price_provider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='product_allowance',
            new_name='income_allowance',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='total_price_income',
            new_name='income_total_price_vatt',
        ),
        migrations.AddField(
            model_name='income',
            name='income_price',
            field=models.CharField(default=2, max_length=255, verbose_name='Стоимость зак. цена * количество'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='income_total_vat',
            field=models.CharField(default=2, max_length=255, verbose_name='Сумма НДС'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='expense_allowance',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Надбавка'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product_price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product_price_provider',
            field=models.CharField(max_length=255, verbose_name='Цена с надбавкой'),
        ),
    ]