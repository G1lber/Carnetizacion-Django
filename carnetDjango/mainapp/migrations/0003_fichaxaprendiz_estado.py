# Generated by Django 5.1.3 on 2025-03-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_usuariopersonalizado_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichaxaprendiz',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
