# Generated by Django 3.2a1 on 2021-03-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0007_rastermetaentry_cloud_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='rasterentry',
            name='ancillary_files',
            field=models.ManyToManyField(to='geodata.ChecksumFile'),
        ),
    ]