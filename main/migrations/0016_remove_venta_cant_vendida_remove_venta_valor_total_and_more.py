# Generated by Django 4.2 on 2023-05-17 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cant_vendida',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='valor_total',
        ),
        migrations.AddField(
            model_name='prefactura',
            name='cantidad',
            field=models.FloatField(null=True, verbose_name='Cantidad a Comprar'),
        ),
    ]
