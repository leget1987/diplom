# Generated by Django 4.0.4 on 2022-05-31 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0004_remove_achievements_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coaching',
            name='coaching_id',
            field=models.AutoField(db_column='id_тренирующегося', primary_key=True, serialize=False, verbose_name='id_тренирующегося'),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(db_column='Описание_группы', verbose_name='Описание_группы'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='practice_id',
            field=models.AutoField(db_column='id_тренировки', primary_key=True, serialize=False, verbose_name='id_тренировки'),
        ),
    ]
