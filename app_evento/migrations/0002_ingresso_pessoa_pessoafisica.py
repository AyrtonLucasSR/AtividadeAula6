# Generated by Django 3.0.3 on 2020-03-13 23:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_evento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingresso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('valor', models.CharField(max_length=50, verbose_name='nome')),
                ('sigla', models.CharField(max_length=50, verbose_name='sigla')),
                ('data_icinio', models.DateTimeField(default=django.utils.timezone.now)),
                ('realizador', models.CharField(max_length=50, verbose_name='realizador')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_evento.Pessoa')),
            ],
            bases=('app_evento.pessoa',),
        ),
    ]
