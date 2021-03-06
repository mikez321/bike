# Generated by Django 3.1.5 on 2021-01-21 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0003_auto_20210120_2027'),
        ('bike', '0003_auto_20210120_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='f_wheel',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wheel.frontwheel'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='r_wheel',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wheel.rearwheel'),
        ),
    ]
