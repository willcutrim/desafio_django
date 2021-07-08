# Generated by Django 3.2.3 on 2021-07-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('sobrenome', models.CharField(max_length=30)),
                ('data_de_admissao', models.DateTimeField(auto_now_add=True)),
                ('status_medico', models.CharField(choices=[(True, 'Ativo'), (False, 'Inativo')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='PostodeTrabalho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_posto', models.CharField(max_length=55)),
                ('endereco', models.CharField(max_length=55)),
                ('status_posto', models.CharField(choices=[(True, 'Ativo'), (False, 'Inativo')], max_length=7)),
            ],
        ),
    ]