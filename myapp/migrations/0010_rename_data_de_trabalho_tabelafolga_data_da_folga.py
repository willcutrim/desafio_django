# Generated by Django 3.2.3 on 2021-07-14 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_tabelafolga'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabelafolga',
            old_name='data_de_trabalho',
            new_name='data_da_folga',
        ),
    ]