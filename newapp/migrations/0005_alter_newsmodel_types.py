# Generated by Django 4.2 on 2023-04-29 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_alter_newsmodel_regions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='types',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.newstype'),
        ),
    ]