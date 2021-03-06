# Generated by Django 3.2.9 on 2022-02-13 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_auto_20220213_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(default='name', max_length=80),
        ),
    ]
