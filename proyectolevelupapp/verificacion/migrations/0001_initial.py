# Generated by Django 4.0.6 on 2022-08-11 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Verificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('dpi', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('verificado', models.BooleanField(blank=True, null=True)),
                ('pose1', models.ImageField(blank=True, null=True, upload_to='')),
                ('pose2', models.ImageField(blank=True, null=True, upload_to='')),
                ('selfie1', models.ImageField(blank=True, null=True, upload_to='')),
                ('selfie2', models.ImageField(blank=True, null=True, upload_to='')),
                ('documento', models.ImageField(blank=True, null=True, upload_to='')),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verificacion.usuario')),
            ],
        ),
    ]
