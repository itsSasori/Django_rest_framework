# Generated by Django 5.0.1 on 2024-01-06 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0003_supreme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supreme',
            old_name='question',
            new_name='name',
        ),
    ]
