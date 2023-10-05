# Generated by Django 4.2.5 on 2023-10-05 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='clients',
            new_name='client',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_vendor',
        ),
        migrations.AddField(
            model_name='income',
            name='product_barcode',
            field=models.CharField(default=2, max_length=255, verbose_name='Штрихкод товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='product_vendor_providers',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Артикул товара поставщика '),
        ),
        migrations.AddField(
            model_name='income',
            name='total_price_income',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10, verbose_name='Полная цена с ндс'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting_app.group', verbose_name='Группа'),
        ),
        migrations.AddField(
            model_name='stock',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting_app.group', verbose_name='Группа'),
        ),
        migrations.AddField(
            model_name='stock',
            name='product_barcode',
            field=models.CharField(default=2, max_length=255, verbose_name='Штрихкод'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='product_country',
            field=models.CharField(default=2, max_length=255, verbose_name='Страна товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='product_nds',
            field=models.CharField(default=2, max_length=255, verbose_name='НДС'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='product_price',
            field=models.CharField(default=2, max_length=255, verbose_name='Общая цена без ндс'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='product_vendor',
            field=models.CharField(default=2, max_length=255, verbose_name='Артикул товара'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_nds',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена продажи с НДС '),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_number',
            field=models.CharField(max_length=100, verbose_name='Номер по накладной'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='expense_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Общая цена с ндс'),
        ),
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_vendor', models.CharField(max_length=100, verbose_name='Артикул товара')),
                ('product_country', models.CharField(max_length=100, verbose_name='Страна товара')),
                ('product_barcode', models.CharField(max_length=100, verbose_name='Штрихкод товара')),
                ('product_nds', models.CharField(max_length=20, verbose_name='НДС')),
                ('product_extra', models.CharField(max_length=100, verbose_name='Надбавка')),
                ('product_quantity', models.CharField(max_length=100, verbose_name='Количество товара')),
                ('price_nds', models.CharField(max_length=100, verbose_name='Общая цена с НДС')),
                ('total_price', models.CharField(max_length=100, verbose_name='Общая цена с ндс и надбавкой')),
                ('date_item', models.DateField(verbose_name='Дата выставления чека')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_app.group', verbose_name='Группа')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_app.product', verbose_name='Товар')),
            ],
        ),
        migrations.CreateModel(
            name='Expense_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_vendor', models.CharField(max_length=100, verbose_name='Артикул товара')),
                ('price_provider', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена поставщика')),
                ('product_quantity', models.CharField(max_length=100, verbose_name='Количество товара для продажи')),
                ('product_nds', models.CharField(max_length=20, verbose_name='НДС')),
                ('product_extra', models.CharField(max_length=100, verbose_name='Надбавка')),
                ('total_price_expense', models.CharField(max_length=100, verbose_name='Общая цена с НДС и надбавкой и количеством')),
                ('product_country', models.CharField(max_length=100, verbose_name='Страна товара')),
                ('product_barcode', models.CharField(max_length=100, verbose_name='Штрихкод товара')),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_app.expense', verbose_name='Расходная накладная')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_app.group', verbose_name='Группа')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_app.product', verbose_name='Товар')),
            ],
        ),
    ]