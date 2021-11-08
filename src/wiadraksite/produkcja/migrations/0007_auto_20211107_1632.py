# Generated by Django 3.2.8 on 2021-11-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkcja', '0006_auto_20211105_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='czujnik',
            name='nazwa',
            field=models.CharField(max_length=50, verbose_name='Nazwa czujnika'),
        ),
        migrations.AlterField(
            model_name='czujnik',
            name='opis',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Opis czujnika'),
        ),
        migrations.AlterField(
            model_name='czujnik',
            name='przykladowy_odczyt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Przykładowa wartość odczytu'),
        ),
        migrations.AlterField(
            model_name='polozenie_czujnika_w_maszynie',
            name='polozenie_czujnika',
            field=models.CharField(choices=[('wejscia', 'Czujnik na wejściu maszyny'), ('wewnetrzny', 'Czujnik oprzyrządowania maszyny'), ('wyjsca', 'Czujnik na wyjściu maszyny')], max_length=10, verbose_name='Położenie czujnika w maszynie'),
        ),
        migrations.AlterField(
            model_name='polozenie_czujnika_w_maszynie',
            name='prefix',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Prefix wartości'),
        ),
        migrations.AlterField(
            model_name='polozenie_czujnika_w_maszynie',
            name='suffix',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Suffix wartości'),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='masa',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='Masa produktu'),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='nazwa',
            field=models.CharField(max_length=50, verbose_name='Nazwa produktu'),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='opis',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Opis produktu'),
        ),
        migrations.AlterField(
            model_name='zlecenie',
            name='data_rozpoczecia',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data rozpoczęcia zlecenia'),
        ),
        migrations.AlterField(
            model_name='zlecenie',
            name='data_zakonczenia',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data zakończenia zlecenia'),
        ),
        migrations.AlterField(
            model_name='zlecenie',
            name='nazwa',
            field=models.CharField(max_length=50, verbose_name='Nazwa zlecenia'),
        ),
        migrations.AlterField(
            model_name='zlecenie',
            name='opis',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Opis zlecenia'),
        ),
        migrations.AlterField(
            model_name='zlecenie',
            name='widoczne',
            field=models.BooleanField(default=True, verbose_name='Czy zlecenie jest widoczne?'),
        ),
    ]