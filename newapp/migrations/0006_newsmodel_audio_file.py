# Generated by Django 4.2 on 2023-04-29 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_alter_newsmodel_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
    ]