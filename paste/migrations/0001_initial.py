# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=30, blank=True)),
                ('syntax', models.IntegerField(default=0, choices=[(0, b'Plain'), (1, b'Python'), (2, b'HTML'), (3, b'SQL'), (4, b'Javascript'), (5, b'CSS')])),
                ('poster', models.CharField(max_length=30, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
