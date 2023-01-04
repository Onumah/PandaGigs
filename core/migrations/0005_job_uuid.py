# Generated by Django 4.0.6 on 2022-12-19 08:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_job_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]