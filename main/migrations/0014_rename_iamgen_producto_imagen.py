# Generated by Django 4.2 on 2023-05-16 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_producto_iamgen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='iamgen',
            new_name='imagen',
        ),
    ]
