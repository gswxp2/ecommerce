# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-15 21:51


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_historicalinvoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalinvoice',
            name='discount_type',
            field=models.CharField(blank=True, choices=[('Percentage', 'Percentage'), ('Fixed', 'Fixed')], default='Percentage', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicalinvoice',
            name='state',
            field=models.CharField(choices=[('Not Paid', 'Not Paid'), ('Paid', 'Paid')], default='Not Paid', max_length=255),
        ),
        migrations.AlterField(
            model_name='historicalinvoice',
            name='type',
            field=models.CharField(blank=True, choices=[('Prepaid', 'Prepaid'), ('Postpaid', 'Postpaid'), ('Bulk purchase', 'Bulk purchase'), ('Not applicable', 'Not applicable')], default='Prepaid', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='discount_type',
            field=models.CharField(blank=True, choices=[('Percentage', 'Percentage'), ('Fixed', 'Fixed')], default='Percentage', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='state',
            field=models.CharField(choices=[('Not Paid', 'Not Paid'), ('Paid', 'Paid')], default='Not Paid', max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='type',
            field=models.CharField(blank=True, choices=[('Prepaid', 'Prepaid'), ('Postpaid', 'Postpaid'), ('Bulk purchase', 'Bulk purchase'), ('Not applicable', 'Not applicable')], default='Prepaid', max_length=255, null=True),
        ),
    ]
