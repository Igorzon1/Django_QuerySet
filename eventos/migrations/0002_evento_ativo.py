# Generated by Django 4.2.20 on 2025-04-03 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
