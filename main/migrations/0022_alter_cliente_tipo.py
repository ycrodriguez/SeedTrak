# Generated by Django 4.2 on 2023-06-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_cliente_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Persona Natural', 'Persona Natural'), ('Entidad Estatal', 'Entidad Estatal')], max_length=255),
        ),
    ]
