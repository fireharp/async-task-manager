# Generated by Django 3.2.9 on 2021-11-05 16:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20211105_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='externaluser',
            name='username',
            field=models.CharField(blank=True, editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='externaluser',
            name='public_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
