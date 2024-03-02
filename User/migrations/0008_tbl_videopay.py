# Generated by Django 5.0 on 2024-03-02 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0007_tbl_adminlogin'),
        ('User', '0007_tbl_star'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_videopay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_seller')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
