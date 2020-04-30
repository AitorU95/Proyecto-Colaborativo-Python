# Generated by Django 3.0.4 on 2020-04-02 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.DateField()),
                ('antiguedad', models.IntegerField(default=0)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEmpresaDjango.Departamento')),
                ('habilidades', models.ManyToManyField(to='appEmpresaDjango.Habilidad')),
            ],
        ),
    ]