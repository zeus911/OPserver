# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opadmin', '0002_auto_20151225_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverfuncateg',
            name='delmark',
            field=models.CharField(default=b'N', max_length=10),
        ),
    ]
