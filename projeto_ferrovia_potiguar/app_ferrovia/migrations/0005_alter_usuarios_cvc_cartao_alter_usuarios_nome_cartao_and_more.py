# Generated by Django 5.0 on 2023-12-06 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ferrovia', '0004_alter_usuarios_c_permissao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='cvc_cartao',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nome_cartao',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='numero_cartao',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='vencimento_cartao',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]