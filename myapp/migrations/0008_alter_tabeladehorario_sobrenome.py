# Generated by Django 3.2.3 on 2021-07-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_tabeladehorario_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabeladehorario',
            name='sobrenome',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]