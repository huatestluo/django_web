# Generated by Django 3.2 on 2021-05-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tsukiko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('practice', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
