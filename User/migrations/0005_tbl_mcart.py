# Generated by Django 5.0 on 2024-01-28 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0003_tbl_material'),
        ('User', '0004_tbl_mbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_mcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('cstatus', models.IntegerField(default=0)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.tbl_material')),
                ('mbooking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_mbooking')),
            ],
        ),
    ]
