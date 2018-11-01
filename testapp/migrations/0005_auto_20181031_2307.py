# Generated by Django 2.1.2 on 2018-10-31 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20181031_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hosts',
            name='AlumFname',
        ),
        migrations.RemoveField(
            model_name='hosts',
            name='EventTitle',
        ),
        migrations.RemoveField(
            model_name='events',
            name='Ehosts',
        ),
        migrations.AlterField(
            model_name='attends',
            name='AlumFname',
            field=models.ForeignKey(default='Admin', on_delete=django.db.models.deletion.CASCADE, to='testapp.Alumni'),
        ),
        migrations.AlterField(
            model_name='attends',
            name='EventTitle',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='testapp.Events'),
        ),
        migrations.DeleteModel(
            name='Hosts',
        ),
    ]
