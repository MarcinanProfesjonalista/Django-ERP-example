# Generated by Django 3.2.8 on 2021-11-05 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produkcja', '0005_auto_20211103_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('opis', models.CharField(blank=True, max_length=50, null=True, verbose_name='Opis maszyny')),
                ('masa', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ilosc_elementow_ze_zlecenia',
            name='id_elementu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkcja.produkt'),
        ),
        migrations.DeleteModel(
            name='Element',
        ),
    ]
