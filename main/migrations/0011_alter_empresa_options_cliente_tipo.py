# Generated by Django 4.2 on 2023-05-15 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_producto_prefactura_remove_venta_cliente_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresa',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresa'},
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Entidad Estatal', 'Entidad Estatal'), ('Persona Natural', 'Persona Natural')], default='Persona Natural', max_length=255),
        ),
    ]
