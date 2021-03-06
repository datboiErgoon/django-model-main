# Generated by Django 4.0.4 on 2022-04-15 01:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zvolte název alba', max_length=100, verbose_name='Název alba')),
                ('hodnoceni', models.IntegerField(help_text='Ohodnoťte album', max_length=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Hodnocení')),
                ('forma', models.CharField(choices=[('LP', 'LP'), ('EP', 'EP'), ('Single', 'Single')], help_text='Zvolte formu alba', max_length=10, verbose_name='Forma alba')),
                ('datumV', models.DateField(help_text='Zvolte datum vydání', verbose_name='Datum vydání')),
            ],
        ),
        migrations.CreateModel(
            name='Certifikace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oceneni', models.CharField(help_text='Zadejte název ocenění', max_length=20, unique=True, verbose_name='Název ocenění')),
            ],
            options={
                'ordering': ['oceneni'],
            },
        ),
        migrations.CreateModel(
            name='Interpret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(help_text='Zadejte jméno umělce', max_length=50, verbose_name='Jméno umělce')),
                ('prijmeni', models.CharField(help_text='Zadejte příjmení umělce', max_length=50, verbose_name='Příjmení umělce')),
                ('narodnost', models.CharField(help_text='Zadejte národnost umělce', max_length=50, verbose_name='Národnost umělce')),
                ('pohlavi', models.CharField(choices=[('Muž', 'Muž'), ('Žena', 'Žena')], help_text='Vyberte pohlaví umělce', max_length=5, verbose_name='Pohlaví umělce')),
                ('datumN', models.DateField(help_text='Vyberte datum narození', verbose_name='Datum narození')),
                ('datumU', models.DateField(blank=True, help_text='Vyberte datum umrtí', null=True, verbose_name='Datum umrtí')),
            ],
            options={
                'ordering': ['prijmeni'],
            },
        ),
        migrations.CreateModel(
            name='Vydavatelstvi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název vydavatelství', max_length=50, unique=True, verbose_name='Název vydavatelství')),
            ],
            options={
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='Zanr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zanr', models.CharField(help_text='Zadejte název žánru', max_length=20, unique=True, verbose_name='Název žánru')),
            ],
            options={
                'ordering': ['zanr'],
            },
        ),
        migrations.CreateModel(
            name='Pisen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název skladby', max_length=100, verbose_name='Název skladby')),
                ('delka', models.TimeField(help_text='Zadejte délku stopy', verbose_name='Délka stopy')),
                ('poradi', models.IntegerField(help_text='Zadejte pořadí stopy', max_length=3, verbose_name='Pořadí stopy')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alba.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='certifikace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alba.certifikace'),
        ),
        migrations.AddField(
            model_name='album',
            name='interpret',
            field=models.ManyToManyField(help_text='Zvolte interpreta', to='alba.interpret'),
        ),
        migrations.AddField(
            model_name='album',
            name='vydavatelstvi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alba.vydavatelstvi'),
        ),
        migrations.AddField(
            model_name='album',
            name='zanr',
            field=models.ManyToManyField(help_text='Zvolte žánry', to='alba.zanr'),
        ),
    ]
