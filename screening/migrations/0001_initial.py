# Generated by Django 2.1 on 2018-09-08 20:15

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chair_number', models.CharField(max_length=3, verbose_name='name')),
                ('status', models.BooleanField(choices=[(0, 'Not reserved chair'), (1, 'Reserved')], default=0, verbose_name='status')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Order', verbose_name='order')),
            ],
            options={
                'verbose_name': 'chair',
                'verbose_name_plural': 'chairs',
            },
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('city', models.CharField(max_length=128, verbose_name='city')),
                ('address', ckeditor.fields.RichTextField(max_length=128, verbose_name='description_city')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='phone_number')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie', verbose_name='movie')),
            ],
            options={
                'verbose_name': 'cinema',
                'verbose_name_plural': 'cinemas',
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
            ],
            options={
                'verbose_name': 'hall',
                'verbose_name_plural': 'halls',
            },
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('price', models.IntegerField(verbose_name='price')),
                ('time_screening', django_jalali.db.models.jDateTimeField(verbose_name='time_screening')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screening.Cinema', verbose_name='cinema')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screening.Hall', verbose_name='hall')),
            ],
            options={
                'verbose_name': 'screening',
                'verbose_name_plural': 'screenings',
            },
        ),
        migrations.AddField(
            model_name='chair',
            name='screening',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screening.Screening', verbose_name='screening'),
        ),
    ]
