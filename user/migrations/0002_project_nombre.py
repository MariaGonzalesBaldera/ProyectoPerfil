# Generated by Django 4.1.4 on 2022-12-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='nombre',
            field=models.CharField(default='Nombre del proyecto', max_length=200),
        ),
    ]
