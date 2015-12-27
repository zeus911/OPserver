# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleList',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('module_name', models.CharField(max_length=60)),
                ('module_caption', models.CharField(max_length=800)),
                ('module_extend', models.CharField(max_length=6000)),
                ('delmark', models.CharField(default=b'N', max_length=10)),
            ],
            options={
                'db_table': 'module_list',
            },
        ),
        migrations.CreateModel(
            name='ServerAppCateg',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('server_categ_id', models.IntegerField()),
                ('app_categ_name', models.CharField(max_length=90)),
                ('delmark', models.CharField(default=b'N', max_length=10)),
            ],
            options={
                'db_table': 'server_app_categ',
            },
        ),
        migrations.CreateModel(
            name='ServerFunCateg',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('server_categ_name', models.CharField(max_length=60)),
                ('delmark', models.CharField(default=b'N', max_length=10)),
            ],
            options={
                'db_table': 'server_fun_categ',
            },
        ),
        migrations.CreateModel(
            name='ServerHostList',
            fields=[
                ('server_host_name', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('server_host_wip', models.CharField(max_length=45)),
                ('server_host_nip', models.CharField(max_length=45)),
                ('server_host_os', models.CharField(max_length=30)),
                ('server_app_id', models.IntegerField()),
                ('delmark', models.CharField(default=b'N', max_length=10)),
            ],
            options={
                'db_table': 'server_host_list',
            },
        ),
    ]
