# Generated by Django 3.0.5 on 2020-05-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_antecedent_patient_terrain_traitement'),
    ]

    operations = [
        migrations.AddField(
            model_name='terrain',
            name='numero',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]