# Generated by Django 2.2.6 on 2019-10-20 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cover',
            name='cover_img',
            field=models.ImageField(default=False, upload_to=''),
        ),
        migrations.AddField(
            model_name='cover',
            name='cover_logo',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]