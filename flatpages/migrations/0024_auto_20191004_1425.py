# Generated by Django 2.1.8 on 2019-10-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0023_auto_20191004_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='dossier_8_cn',
            field=models.TextField(blank=True, null=True, verbose_name='dossier 8 content'),
        ),
        migrations.AddField(
            model_name='flatpage',
            name='dossier_8_img',
            field=models.ImageField(null=True, upload_to='', verbose_name='dossier 8 image'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='dossier_1_cn',
            field=models.TextField(blank=True, null=True, verbose_name='dossier 1 content'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='dossier_2_cn',
            field=models.TextField(blank=True, null=True, verbose_name='dossier 2 content'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='dossier_3_cn',
            field=models.TextField(blank=True, null=True, verbose_name='dossier 3 content'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='dossier_4_cn',
            field=models.TextField(blank=True, null=True, verbose_name='dossier 4 content'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='dossier_5_cn',
            field=models.TextField(blank=True, null=True, verbose_name='dossier 5 content'),
        ),
    ]
