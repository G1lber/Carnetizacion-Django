# Generated by Django 5.0.2 on 2025-02-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariopersonalizado',
            name='is_active',
            field=models.IntegerField(default=True),
        ),
    ]
