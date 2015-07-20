# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoundImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('output_image_file_path', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InputImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input_image_file_path', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='foundimages',
            name='input_image',
            field=models.ForeignKey(to='search.InputImage'),
        ),
    ]
