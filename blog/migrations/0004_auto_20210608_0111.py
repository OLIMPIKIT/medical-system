# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210607_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(verbose_name='Специализация', to='blog.Specialization'),
        ),
        migrations.AlterField(
            model_name='reception',
            name='doctor',
            field=models.ForeignKey(verbose_name='Врач', to='blog.Doctor'),
        ),
        migrations.AlterField(
            model_name='reception',
            name='patient_info',
            field=models.CharField(verbose_name='Информация о пациенте ', max_length=10000),
        ),
    ]
