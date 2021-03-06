# Generated by Django 2.2.3 on 2020-04-16 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_colaborativo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto_colaborativo.ticket'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='apellido',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto_colaborativo.Empleado'),
        ),
    ]
