# Generated by Django 3.1 on 2020-09-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='id_cat',
            field=models.AutoField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='Histoire',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='agriculture',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='animaux',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='blessures',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='bourse',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='covid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='culture',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='célébrité',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='divertissement',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='economie',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='education',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='eid_el_adha',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='espace',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='football',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='id_cat',
            field=models.AutoField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='immobilier',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='local_trends',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='loi_décret',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='meteo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='monde',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='nature',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='parlement',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='parties_politiques',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='politique',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='religion',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='revue',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='revue_presse',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='revue_web',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='rumeurs',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='réseaux_sociaux',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='santé',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='science',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='société',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='sport',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='statistiques',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='terrorisme',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category_info',
            name='tourisme',
            field=models.BooleanField(default=False),
        ),
    ]
