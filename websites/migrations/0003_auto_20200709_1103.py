# Generated by Django 3.0.8 on 2020-07-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0002_auto_20200709_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='meta_description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]