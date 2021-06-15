# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210608_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reception',
            name='specialization',
            field=models.ForeignKey(verbose_name='Специализация', to='blog.Specialization'),
        ),
    ]
