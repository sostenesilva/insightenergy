# Generated by Django 5.0.4 on 2024-05-05 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0010_alter_irradiacao_atualização'),
    ]

    operations = [
        migrations.AlterField(
            model_name='irradiacao',
            name='atualização',
            field=models.DateField(default=datetime.date(2024, 5, 5)),
        ),
    ]
