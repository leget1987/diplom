# Generated by Django 4.0.4 on 2022-05-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0002_alter_achievements_belt_alter_achievements_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='speaker_id',
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(db_column='Номер телефона', max_length=20, verbose_name='Номер телефона'),
        ),
    ]