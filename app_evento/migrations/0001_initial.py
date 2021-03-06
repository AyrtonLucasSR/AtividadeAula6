# Generated by Django 3.0.3 on 2020-03-13 23:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('sigla', models.CharField(max_length=50, verbose_name='sigla')),
                ('data_icinio', models.DateTimeField(default=django.utils.timezone.now)),
                ('realizador', models.CharField(max_length=50, verbose_name='realizador')),
                ('descricao', models.TextField()),
            ],
        ),
    ]
