# Generated by Django 4.1.3 on 2022-11-02 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0003_rename_cust_id_sales_order_customer_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='product_id',
            new_name='product_name',
        ),
    ]