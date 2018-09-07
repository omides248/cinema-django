# Generated by Django 2.1 on 2018-09-07 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('screening', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chair',
            options={'verbose_name': 'chair', 'verbose_name_plural': 'chairs'},
        ),
        migrations.AlterModelOptions(
            name='cinema',
            options={'verbose_name': 'cinema', 'verbose_name_plural': 'cinemas'},
        ),
        migrations.AlterModelOptions(
            name='hall',
            options={'verbose_name': 'hall', 'verbose_name_plural': 'halls'},
        ),
        migrations.AlterModelOptions(
            name='screening',
            options={'verbose_name': 'screening', 'verbose_name_plural': 'screenings'},
        ),
        migrations.AlterField(
            model_name='chair',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Order'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screening.Cinema'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screening.Hall'),
        ),
    ]
