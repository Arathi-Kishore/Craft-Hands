# Generated by Django 5.0 on 2024-01-05 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_alter_tbl_user_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_user',
            old_name='location_id',
            new_name='location',
        ),
    ]