# Generated by Django 4.0.4 on 2022-05-14 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Belt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Пояс', max_length=20)),
            ],
            options={
                'verbose_name': 'Пояс',
                'verbose_name_plural': 'Пояса',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(db_column='Фамилия', max_length=30)),
                ('firstname', models.CharField(db_column='Имя', max_length=30)),
                ('patronymic', models.CharField(db_column='Отчество', max_length=30)),
                ('date_birth', models.DateTimeField(db_column='Дата рождения')),
                ('phone_number', models.CharField(db_column='Номер телефона', max_length=20)),
                ('date_enrollment', models.DateTimeField(db_column='Дата зачисления')),
                ('growth', models.CharField(db_column='Рост', max_length=10)),
                ('weight', models.CharField(db_column='Вес', max_length=10)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(db_column='Фамилия', max_length=30)),
                ('firstname', models.CharField(db_column='Имя', max_length=30)),
                ('patronymic', models.CharField(db_column='Отчество', max_length=30)),
                ('phone_number', models.CharField(db_column='Номер телефона', max_length=30)),
                ('date_birth', models.DateTimeField(db_column='Дата рождения')),
                ('date_enrollment', models.DateTimeField(db_column='Дата зачисления')),
            ],
            options={
                'verbose_name': 'Тренер',
                'verbose_name_plural': 'Тренеры',
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_competition', models.BooleanField(db_column='Аттестация')),
                ('date', models.DateField(db_column='Дата')),
                ('time', models.TimeField(db_column='Время')),
                ('place', models.CharField(db_column='Место проведения', max_length=50)),
                ('cost', models.CharField(db_column='Стоимость', max_length=20)),
                ('coach_id', models.ForeignKey(db_column='Тренер', on_delete=django.db.models.deletion.CASCADE, to='diplom.coach')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятии',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Наименование', max_length=50)),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_formation', models.DateTimeField(db_column='Дата формирования')),
                ('description', models.TextField(db_column='Описание')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Название зала', max_length=50)),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
        ),
        migrations.CreateModel(
            name='PackageDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(db_column='Пакет документов', on_delete=django.db.models.deletion.CASCADE, to='diplom.document')),
            ],
            options={
                'verbose_name': 'Пакет документов',
                'verbose_name_plural': 'Пакеты документов',
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Разряд', max_length=50)),
            ],
            options={
                'verbose_name': 'Разряд',
                'verbose_name_plural': 'Разряды',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Рейтинг', max_length=50)),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='TypeStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Тип заявления', max_length=30)),
            ],
            options={
                'verbose_name': 'Тип заявления',
                'verbose_name_plural': 'Типы заявления',
            },
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_statement', models.DateTimeField(db_column='Дата заявления')),
                ('contract_number', models.CharField(db_column='Номер договора', max_length=20)),
                ('data_start_contract', models.DateTimeField(db_column='Дата начала договора')),
                ('data_stop_contract', models.DateTimeField(db_column='Дата окончания договора')),
                ('payment_status', models.BooleanField(db_column='Статус оплаты', default=False)),
                ('passport_series', models.CharField(db_column='Серия паспорта', max_length=20)),
                ('passport_number', models.CharField(db_column='Номер паспорта', max_length=20)),
                ('client', models.ForeignKey(db_column='Клиент', on_delete=django.db.models.deletion.CASCADE, to='diplom.client')),
                ('package_documents', models.ForeignKey(db_column='Пакет документов', on_delete=django.db.models.deletion.CASCADE, to='diplom.packagedocuments')),
                ('type_statement', models.ForeignKey(db_column='Тип заявления', on_delete=django.db.models.deletion.CASCADE, to='diplom.typestatement')),
            ],
            options={
                'verbose_name': 'Заявление',
                'verbose_name_plural': 'Заявления',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition_id', models.ForeignKey(db_column='Мероприятие', on_delete=django.db.models.deletion.CASCADE, to='diplom.competition')),
                ('entry', models.ForeignKey(db_column='Запись', on_delete=django.db.models.deletion.CASCADE, to='diplom.entry')),
            ],
            options={
                'verbose_name': 'Выступающий',
                'verbose_name_plural': 'Выступающие',
            },
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_column='Дата')),
                ('time', models.TimeField(db_column='Время')),
                ('cost', models.CharField(db_column='Стоимость', max_length=20)),
                ('coach', models.ForeignKey(db_column='Тренер', on_delete=django.db.models.deletion.CASCADE, to='diplom.coach')),
                ('hall', models.ForeignKey(db_column='Зал', on_delete=django.db.models.deletion.CASCADE, to='diplom.hall')),
            ],
            options={
                'verbose_name': 'Тренировка',
                'verbose_name_plural': 'Тренировки',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='group',
            field=models.ForeignKey(db_column='Группа', on_delete=django.db.models.deletion.CASCADE, to='diplom.group'),
        ),
        migrations.AddField(
            model_name='entry',
            name='statement',
            field=models.ForeignKey(db_column='Заявление', on_delete=django.db.models.deletion.CASCADE, to='diplom.statement'),
        ),
        migrations.AddField(
            model_name='competition',
            name='rating_id',
            field=models.ForeignKey(db_column='Рейтинг', on_delete=django.db.models.deletion.CASCADE, to='diplom.rating'),
        ),
        migrations.AddField(
            model_name='competition',
            name='speaker_id',
            field=models.ForeignKey(db_column='Выступающий', on_delete=django.db.models.deletion.CASCADE, to='diplom.speaker'),
        ),
        migrations.CreateModel(
            name='Coaching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.ForeignKey(db_column='Запись', on_delete=django.db.models.deletion.CASCADE, to='diplom.entry')),
                ('practice_id', models.ForeignKey(db_column='Тренировка', on_delete=django.db.models.deletion.CASCADE, to='diplom.practice')),
            ],
            options={
                'verbose_name': 'Тренирующий',
                'verbose_name_plural': 'Тренирующие',
            },
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assignment', models.DateTimeField(db_column='Дата присвоения')),
                ('passport_number', models.CharField(db_column='Номер паспорта спортсмена', max_length=20)),
                ('belt', models.ForeignKey(db_column='Пояс', on_delete=django.db.models.deletion.CASCADE, to='diplom.belt')),
                ('client', models.ForeignKey(db_column='Клиент', on_delete=django.db.models.deletion.CASCADE, to='diplom.client')),
                ('competition', models.ForeignKey(db_column='Соревнование', on_delete=django.db.models.deletion.CASCADE, to='diplom.competition')),
                ('rank', models.ForeignKey(db_column='Разряд', on_delete=django.db.models.deletion.CASCADE, to='diplom.rank')),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
    ]