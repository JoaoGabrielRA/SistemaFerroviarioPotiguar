# Generated by Django 5.0 on 2023-12-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('senha', models.CharField(max_length=150)),
                ('c_permissao', models.BooleanField(default=False)),
                ('g_permissao', models.BooleanField(default=False)),
                ('nome_cartao', models.CharField(max_length=150)),
                ('numero_cartao', models.CharField(max_length=150)),
                ('vencimento_cartao', models.CharField(max_length=150)),
                ('cvc_cartao', models.CharField(max_length=3)),
            ],
        ),
    ]
