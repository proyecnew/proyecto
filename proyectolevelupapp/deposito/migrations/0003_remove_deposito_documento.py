# Generated by Django 4.0.6 on 2022-08-18 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deposito', '0002_persona_alter_deposito_persona_delete_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposito',
            name='documento',
        ),
    ]