# Generated by Django 5.0.4 on 2024-05-07 05:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_alter_vendor_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.UUIDField(default=uuid.UUID('78f37663-7e58-44d2-a5c4-8f87d8b03911'), editable=False, unique=True),
        ),
    ]