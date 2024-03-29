# Generated by Django 2.2.6 on 2019-10-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20191021_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='shows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shows_heading', models.CharField(max_length=50)),
                ('shows_decription', models.CharField(max_length=300)),
                ('shows_poster', models.ImageField(default='', upload_to='')),
                ('shows_name', models.CharField(max_length=50)),
                ('shows_date', models.DateField()),
                ('shows_start_time', models.TimeField()),
                ('shows_end_time', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='cover',
            name='cover_heading',
            field=models.CharField(max_length=50),
        ),
    ]
