# Generated by Django 3.0.7 on 2020-07-15 13:36

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0008_auto_20200714_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                (
                    'modifiableentry_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='geodata.ModifiableEntry',
                    ),
                ),
                ('caption', models.CharField(blank=True, max_length=100, null=True)),
                ('label', models.CharField(blank=True, max_length=100, null=True)),
                ('bounding_box', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                (
                    'feature',
                    django.contrib.gis.db.models.fields.GeometryField(null=True, srid=4326),
                ),
                ('annotator', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                (
                    'raster',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='geodata.RasterEntry'
                    ),
                ),
            ],
            bases=('geodata.modifiableentry',),
        ),
    ]
