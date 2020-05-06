# Generated by Django 3.0.6 on 2020-05-06 20:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20200506_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreresult',
            name='data',
            field=models.FileField(default=django.utils.timezone.now, upload_to='scores'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scoreresult',
            name='log',
            field=models.FileField(blank=True, null=True, upload_to='scores_logs'),
        ),
        migrations.AlterField(
            model_name='scoreresult',
            name='overall_score',
            field=models.FloatField(blank=True, default=0.9, null=True),
        ),
    ]
