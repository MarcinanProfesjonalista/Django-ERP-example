# Generated by Django 3.2.8 on 2021-10-28 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Czujnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('opis', models.CharField(blank=True, max_length=50, null=True)),
                ('przykladowy_odczyt', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('opis', models.CharField(blank=True, max_length=50, null=True)),
                ('masa', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ilosc_elementow_ze_zlecenia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc_elementow', models.DecimalField(decimal_places=0, max_digits=6)),
                ('id_elementu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkcja.element')),
            ],
        ),
        migrations.CreateModel(
            name='Maszyna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('opis', models.CharField(blank=True, max_length=50, null=True)),
                ('wydajnosc', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zlecenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('opis', models.CharField(blank=True, max_length=50, null=True)),
                ('data_rozpoczecia', models.DateTimeField(blank=True, null=True)),
                ('data_zakonczenia', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Polozenie_czujnika_w_maszynie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polozenie_czujnika', models.CharField(choices=[('Wejścia', 'Wejścia'), ('Wewnętrzny', 'Wewnętrzny'), ('Wyjścia', 'Wyjścia')], max_length=10)),
                ('prefix', models.CharField(blank=True, max_length=50, null=True)),
                ('suffix', models.CharField(blank=True, max_length=50, null=True)),
                ('id_czujnika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkcja.czujnik')),
                ('id_maszyny', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkcja.maszyna')),
            ],
        ),
        migrations.CreateModel(
            name='ilosc_elementow_ze_zlecenia_ma_przejsc_przez_maszyne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_per_element', models.DurationField(blank=True, null=True)),
                ('id_maszyny', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkcja.maszyna')),
                ('id_zlecenia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkcja.ilosc_elementow_ze_zlecenia')),
            ],
        ),
        migrations.AddField(
            model_name='ilosc_elementow_ze_zlecenia',
            name='id_zlecenia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkcja.zlecenie'),
        ),
    ]