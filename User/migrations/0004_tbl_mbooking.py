# Generated by Django 5.0 on 2024-01-28 04:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_tbl_seller'),
        ('User', '0003_rename_user_id_tbl_wbooking_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_mbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]