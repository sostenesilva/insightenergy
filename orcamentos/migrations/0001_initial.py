# Generated by Django 5.0.4 on 2024-05-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Irradiacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=50)),
                ('irr', models.TextField()),
            ],
        ),
    ]
