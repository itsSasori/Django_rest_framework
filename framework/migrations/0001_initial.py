# Generated by Django 5.0.1 on 2024-01-04 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advocate',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('bio', models.TextField(null=True)),
            ],
        ),
    ]
