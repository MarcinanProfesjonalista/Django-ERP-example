# Generated by Django 3.1.2 on 2021-11-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkcja', '0013_auto_20211109_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='czujnik',
            name='nazwa',
            field=models.CharField(default='', max_length=50, verbose_name='Nazwa czujnika'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='czujnik',
            name='opis',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Opis czujnika'),
        ),
        migrations.AddField(
            model_name='czujnik',
            name='polozenie_czujnika',
            field=models.CharField(choices=[('ciagly', 'Licznik(pomiar ciągły)'), ('chwilowy', 'Termometr(pomiar chwilowy)'), ('masy_ciagly', 'Waga(pomiar sumowany)'), ('masy_chwilowy', 'Waga')], default='Czujnik', max_length=50, verbose_name='Rodzaj czujnika'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='czujnik',
            name='przykladowy_odczyt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Przykładowa wartość odczytu'),
        ),
        migrations.AlterField(
            model_name='polozenie_czujnika_w_maszynie',
            name='polozenie_czujnika',
            field=models.CharField(choices=[('wejscia', 'Czujnik na wejściu maszyny'), ('wewnetrzny', 'Czujnik oprzyrządowania maszyny'), ('wyjsca', 'Czujnik na wyjściu maszyny')], max_length=50, verbose_name='Położenie czujnika w maszynie'),
        ),
    ]