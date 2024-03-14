# Generated by Django 5.0.3 on 2024-03-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sensor', models.BooleanField(default=False)),
                ('Botao', models.BooleanField(default=False)),
                ('LigaRobo', models.BooleanField(default=False)),
                ('ResetContador', models.BooleanField(default=False)),
                ('ValorContagem', models.IntegerField(default=0)),
            ],
        ),
    ]
