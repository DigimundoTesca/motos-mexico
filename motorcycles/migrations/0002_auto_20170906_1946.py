# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders_entry', '0006_entryorder_motorcycle_owner'),
        ('motorcycles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusMotorcyclePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='StatusOptions',
            new_name='DamageStatusOptions',
        ),
        migrations.RemoveField(
            model_name='statuspart',
            name='entry_order',
        ),
        migrations.RemoveField(
            model_name='statuspart',
            name='motorcycle_part',
        ),
        migrations.RemoveField(
            model_name='statuspart',
            name='status_option',
        ),
        migrations.DeleteModel(
            name='StatusPart',
        ),
        migrations.AddField(
            model_name='statusmotorcyclepart',
            name='damage_status_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motorcycles.DamageStatusOptions'),
        ),
        migrations.AddField(
            model_name='statusmotorcyclepart',
            name='entry_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders_entry.EntryOrder'),
        ),
        migrations.AddField(
            model_name='statusmotorcyclepart',
            name='motorcycle_part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motorcycles.MotorcyclePart'),
        ),
    ]
