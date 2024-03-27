# Generated by Django 5.0.1 on 2024-03-14 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapporders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_adress',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='price_per_item',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=12),
        ),
    ]