# Generated by Django 2.1.8 on 2019-09-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0005_auto_20190930_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flatpage',
            old_name='luminocity',
            new_name='luminosity',
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='title',
            field=models.CharField(max_length=300, verbose_name='title'),
        ),
    ]
