# Generated by Django 3.2.3 on 2021-07-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_tabeladehorario_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabeladehorario',
            name='nome',
            field=models.CharField(choices=[('willyam', 'nome')], max_length=45),
        ),
    ]
