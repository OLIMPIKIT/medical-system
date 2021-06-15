# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='info',
            field=models.CharField(verbose_name='Информация о враче', max_length=10000),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(verbose_name='Врач ', to='blog.Specialization'),
        ),
        migrations.AlterField(
            model_name='reception',
            name='doctor',
            field=models.ForeignKey(verbose_name='Врач ', to='blog.Doctor'),
        ),
    ]
