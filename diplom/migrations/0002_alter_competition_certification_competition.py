# Generated by Django 4.0.4 on 2022-05-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='certification_competition',
            field=models.CharField(choices=[('COMP', 'Соревнование'), ('CERF', 'Аттестациия')], db_column='Аттестация_соревнования', max_length=20, verbose_name='Аттестация_соревнования'),
        ),
    ]
