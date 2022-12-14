# Generated by Django 4.1.3 on 2022-11-02 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0002_remove_customer_city_remove_customer_company_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales_order',
            old_name='cust_id',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='sales_order',
            old_name='sales_person_id',
            new_name='sales_person_name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
