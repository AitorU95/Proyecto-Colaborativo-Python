# Generated by Django 2.2.3 on 2020-05-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_colaborativo', '0008_delete_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
