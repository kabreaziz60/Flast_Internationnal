# Generated by Django 4.1.1 on 2022-10-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ville_depart', models.CharField(max_length=100)),
                ('Ville_liavraison', models.CharField(max_length=100)),
                ('Poid_total', models.CharField(max_length=100)),
                ('Dimension', models.CharField(max_length=100)),
                ('Nom', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('Telephone', models.CharField(max_length=100)),
                ('Message', models.TextField()),
            ],
        ),
    ]
