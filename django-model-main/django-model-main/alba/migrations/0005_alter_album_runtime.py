# Generated by Django 4.0.4 on 2022-06-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alba', '0004_album_runtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='runtime',
            field=models.IntegerField(null=True, verbose_name='Délka alba'),
        ),
    ]