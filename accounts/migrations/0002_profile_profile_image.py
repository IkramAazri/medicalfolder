# Generated by Django 3.0.5 on 2020-05-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profil_defaut.png', null=True, upload_to='users/'),
        ),
    ]