# Generated by Django 3.2.9 on 2021-11-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_externaluser'),
    ]

    operations = [
        migrations.AddField(
            model_name='externaluser',
            name='role',
            field=models.CharField(blank=True, editable=False, max_length=32),
        ),
    ]
