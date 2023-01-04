# Generated by Django 4.0.6 on 2022-12-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=225)),
                ('Job', models.CharField(max_length=225)),
                ('Location', models.CharField(max_length=225)),
                ('ContactEmail', models.CharField(max_length=225)),
                ('WebUrl', models.URLField()),
                ('Tags', models.CharField(max_length=225)),
                ('Logo', models.ImageField(upload_to='')),
                ('Description', models.TextField()),
            ],
        ),
    ]