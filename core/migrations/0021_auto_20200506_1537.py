# Generated by Django 3.0.6 on 2020-05-06 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20200506_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreresult',
            name='overall_score',
            field=models.FloatField(default=0.8693398356764417),
        ),
    ]
