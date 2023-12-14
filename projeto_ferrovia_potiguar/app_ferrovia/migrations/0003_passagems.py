# Generated by Django 5.0 on 2023-12-06 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ferrovia', '0002_viagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passagems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=150)),
                ('cpf_passageiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ferrovia.usuarios')),
                ('id_viagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ferrovia.viagem')),
            ],
        ),
    ]