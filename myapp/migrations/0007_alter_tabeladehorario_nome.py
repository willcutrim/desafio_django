# Generated by Django 3.2.3 on 2021-07-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_tabeladehorario_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabeladehorario',
            name='nome',
            field=models.CharField(max_length=45),
        ),
    ]