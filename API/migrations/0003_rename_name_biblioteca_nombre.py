# Generated by Django 4.0.6 on 2022-08-02 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_biblioteca_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biblioteca',
            old_name='name',
            new_name='nombre',
        ),
    ]
