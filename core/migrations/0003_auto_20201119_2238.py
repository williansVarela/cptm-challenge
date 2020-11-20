# Generated by Django 3.1.3 on 2020-11-20 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_line'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='line',
            options={'verbose_name': 'Linha', 'verbose_name_plural': 'Linhas'},
        ),
        migrations.AddField(
            model_name='line',
            name='number',
            field=models.IntegerField(null=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='line',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
    ]