# Generated by Django 2.1.2 on 2019-06-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Negocio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='usuario',
            field=models.ManyToManyField(to='Negocio.Usuario'),
        ),
    ]