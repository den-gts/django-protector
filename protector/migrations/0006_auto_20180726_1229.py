# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-26 12:29
from __future__ import unicode_literals

from django.db import migrations

def forwards_func(apps, schema_editor):
    OwnerToPermission = apps.get_model("protector", "OwnerToPermission")
    OwnerToPermission.objects.filter(content_type_id=1).update(content_type=None)
    OwnerToPermission.objects.filter(object_id=0).update(object_id=None)

def backwards_func(apps, schema_editor):
    OwnerToPermission = apps.get_model("protector", "OwnerToPermission")
    OwnerToPermission.objects.filter(content_type_id__isnull=True).update(content_type=1)
    OwnerToPermission.objects.filter(object_id__isnull=True).update(object_id=0)


class Migration(migrations.Migration):

    dependencies = [
        ('protector', '0005_auto_20180725_1629'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func)
    ]
