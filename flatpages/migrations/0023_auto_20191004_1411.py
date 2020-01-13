# Generated by Django 2.1.8 on 2019-10-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0022_auto_20191004_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='dossier_7_cn',
            field=models.TextField(blank=True, null=True, verbose_name='dossier 7 content'),
        ),
        migrations.AddField(
            model_name='flatpage',
            name='dossier_7_img',
            field=models.ImageField(null=True, upload_to='', verbose_name='dossier 7 image'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='dossier_6_cn',
            field=models.TextField(blank=True, null=True, verbose_name='dossier 6 content'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='dossier_6_img',
            field=models.ImageField(null=True, upload_to='', verbose_name='dossier 6 image'),
        ),
    ]
