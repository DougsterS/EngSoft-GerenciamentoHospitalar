# Generated by Django 2.2.2 on 2019-06-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_auto_20190616_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='funcao',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
