# Generated by Django 5.1.5 on 2025-05-02 14:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_code_expired_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='expired_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
