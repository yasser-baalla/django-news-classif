# Generated by Django 3.1 on 2020-09-04 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200904_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category_info',
            old_name='football',
            new_name='Football',
        ),
        migrations.RenameField(
            model_name='category_info',
            old_name='local_trends',
            new_name='Local_Trends',
        ),
        migrations.RenameField(
            model_name='category_info',
            old_name='blessures',
            new_name='blessures_accidents_et_décès',
        ),
        migrations.RenameField(
            model_name='category_info',
            old_name='loi_décret',
            new_name='loi_et_décret',
        ),
        migrations.RenameField(
            model_name='category_info',
            old_name='revue_presse',
            new_name='revue_de_presse',
        ),
        migrations.RenameField(
            model_name='category_info',
            old_name='revue_web',
            new_name='revue_du_web',
        ),
    ]
