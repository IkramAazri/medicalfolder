# Generated by Django 3.0.5 on 2020-05-12 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalStaff', '0003_auto_20200512_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='avisMedical',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='consultation',
            name='dateDebutCertificat',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consultation',
            name='dateFinCertificat',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consultation',
            name='nbrJour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consultation',
            name='ordonnance',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
