# Generated by Django 4.2 on 2023-04-27 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_alter_newsmodel_short_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.regionmodel'),
        ),
    ]