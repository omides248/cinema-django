# Generated by Django 2.1 on 2018-09-07 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20180904_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='film',
            new_name='movie',
        ),
    ]
