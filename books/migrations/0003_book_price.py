# Generated by Django 5.1.5 on 2025-03-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=12000),
        ),
    ]
