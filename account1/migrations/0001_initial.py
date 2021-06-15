# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('role', models.CharField(verbose_name='Пол', max_length=40, blank=True, choices=[('0', 'Пациент'), ('1', 'Врач'), ('2', 'Регистратор'), ('3', 'Администратор')])),
                ('surname', models.CharField(verbose_name='Фамилия', max_length=50, blank=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=50, blank=True)),
                ('patronym', models.CharField(verbose_name='Отчество', max_length=50, blank=True)),
                ('gender', models.CharField(verbose_name='Пол', max_length=40, blank=True, choices=[('M', 'Мужcкой'), ('F', 'Женский')])),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения', blank=True, null=True)),
                ('snils', models.CharField(verbose_name='Номер СНИЛС', max_length=11, blank=True)),
                ('passport', models.CharField(verbose_name='Серия и номер паспорта', max_length=10, blank=True)),
                ('adress', models.CharField(verbose_name='Адрес', max_length=300, blank=True)),
                ('phone', models.CharField(verbose_name='Телефон', max_length=11, blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
