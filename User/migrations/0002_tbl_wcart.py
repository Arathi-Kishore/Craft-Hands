# Generated by Django 5.0 on 2024-01-27 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0002_tbl_wgallery'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_wcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('cstatus', models.IntegerField(default=0)),
                ('wbooking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_wbooking')),
                ('works_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.tbl_work')),
            ],
        ),
    ]