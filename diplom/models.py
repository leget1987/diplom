from django.db import models


# Create your models here.
class Group(models.Model):
    group_id = models.AutoField(primary_key=True, db_column="id_группы", verbose_name="id_группы")
    data_formation = models.DateField(db_column='Дата_формирования', verbose_name="Дата_формирования")
    description = models.TextField(db_column="Описание_групы", verbose_name="Описание_группы")

    def __str__(self):
        return f'{self.description}'

    class Meta:
        db_table = 'Группа'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Entry(models.Model):
    entry_id = models.AutoField(primary_key=True, db_column="id_записи", verbose_name="id_записи")
    group = models.ForeignKey(to='Group', on_delete=models.CASCADE, db_column="Группа", verbose_name="Группа")
    statement = models.ForeignKey(to='Statement', on_delete=models.CASCADE, db_column="Заявление",
                                  verbose_name="Заявление")

    def __str__(self):
        return f'Запись в группу {self.group.description}'

    class Meta:
        db_table = 'Запись'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Statement(models.Model):
    statement_id = models.AutoField(primary_key=True, db_column="id_заявление", verbose_name="id_заявление")
    client = models.ForeignKey(to='Client', on_delete=models.CASCADE, db_column="id_клиента(FK)",
                               verbose_name="id_клиента(FK)")
    type_statement = models.ForeignKey(to='TypeStatement', on_delete=models.CASCADE, db_column="id_тип_заявления(FK)",
                                       verbose_name="id_тип_заявления(FK)")
    data_statement = models.DateField(db_column="Дата_заявления", verbose_name="Дата_заявления")
    contract_number = models.CharField(max_length=20, db_column="Номер_договора", verbose_name="Номер_договора")
    data_start_contract = models.DateField(db_column="Дата_начала_договора", verbose_name="Дата_начала_договора")
    data_stop_contract = models.DateField(db_column="Дата_окончания_договора", verbose_name="Дата_окончания_договора")
    payment_status = models.BooleanField(default=False, db_column="Состояние_оплаты", verbose_name="Состояние_оплаты")
    passport_series = models.CharField(max_length=20, db_column="Серия_паспорта", verbose_name="Серия_паспорта")
    passport_number = models.CharField(max_length=20, db_column="Номер_паспорта", verbose_name="Номер_паспорта")

    def __str__(self):
        return f'Заявление на {self.type_statement} от {self.client}'

    class Meta:
        db_table = 'Заявления'
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'


class TypeStatement(models.Model):
    type_statement_id = models.AutoField(primary_key=True, db_column="id_тип_заявление",
                                         verbose_name="id_тип_заявление")
    name = models.CharField(max_length=30, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Тип_заявления'
        verbose_name = 'Тип заявления'
        verbose_name_plural = 'Типы заявления'


class PackageDocuments(models.Model):
    package_document_id = models.AutoField(primary_key=True, db_column="id_пакет_документов",
                                           verbose_name="id_пакет_документов")
    document = models.ForeignKey(to='Document', on_delete=models.CASCADE, db_column="id_документа(FK)",
                                 verbose_name="id_документа(FK)")
    statement = models.ForeignKey(to='Statement', on_delete=models.CASCADE, db_column="id_заявления(FK)",
                                  verbose_name="id_заявления(FK)")

    def __str__(self):
        return 'Пакет документов'

    class Meta:
        db_table = 'Пакет_документов'
        verbose_name = 'Пакет документов'
        verbose_name_plural = 'Пакеты документов'


class Document(models.Model):
    document_id = models.AutoField(primary_key=True, db_column="id_документа", verbose_name="id_документа")
    name = models.CharField(max_length=50, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Документы'
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Client(models.Model):
    client_id = models.AutoField(primary_key=True, db_column="id_клиента", verbose_name="id_клиента")
    surname = models.CharField(max_length=30, db_column="Фамилия", verbose_name="Фамилия")
    firstname = models.CharField(max_length=30, db_column="Имя", verbose_name="Имя")
    patronymic = models.CharField(max_length=30, db_column="Отчество", verbose_name="Отчество")
    date_birth = models.DateField(db_column="Дата_рождения", verbose_name="Дата_рождения")
    phone_number = models.CharField(max_length=20, db_column="Телефон", verbose_name="Телефон")
    date_enrollment = models.DateField(db_column="Дата_зачисления", verbose_name="Дата_зачисления")
    growth = models.CharField(max_length=10, db_column="Рост", verbose_name="Рост")
    weight = models.CharField(max_length=10, db_column="Вес", verbose_name="Вес")

    def __str__(self):
        return f"Клиент {self.surname}"

    class Meta:
        db_table = 'Клиент'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Achievements(models.Model):
    achievements_id = models.AutoField(primary_key=True, db_column="id_достижения", verbose_name="id_достижения")
    client = models.ForeignKey(to='Client', on_delete=models.CASCADE, db_column="id_клиента(FK)",
                               verbose_name="id_клиента(FK)")
    rank = models.ForeignKey(to='Rank', on_delete=models.CASCADE, db_column="id_разряда(FK)",
                             verbose_name="id_разряда(FK)")
    date_assignment = models.DateField(db_column="Дата_присвоения", verbose_name="Дата_присвоения")
    belt = models.ForeignKey(to='Belt', on_delete=models.CASCADE, db_column="id_пояса(FK)", verbose_name="id_пояса(FK)")
    competition = models.ForeignKey(to='Competition', on_delete=models.CASCADE, db_column="id_мероприятия(FK)",
                                    verbose_name="id_мероприятия(FK)")
    passport_number = models.CharField(max_length=20, db_column="Номер_паспорта_спортсмена",
                                       verbose_name="Номер_паспорта_спортсмена")

    def __str__(self):
        return f'Достижение клиента {self.client}'

    class Meta:
        db_table = 'Достижения'
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class Belt(models.Model):
    belt_id = models.AutoField(primary_key=True, db_column="id_пояса", verbose_name="id_пояса")
    name = models.CharField(max_length=20, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Пояс'
        verbose_name = 'Пояс'
        verbose_name_plural = 'Пояса'
        ordering = ('name',)


class Rank(models.Model):
    rank_id = models.AutoField(primary_key=True, db_column="id_разряда", verbose_name="id_разряда")
    name = models.CharField(max_length=50, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Разряд'
        verbose_name = 'Разряд'
        verbose_name_plural = 'Разряды'


class Competition(models.Model):
    COMPETITION = 'COMP'
    CERTIFICATION = 'CERF'
    TYPE_COMPETITION = (
        (COMPETITION, 'Соревнование'),
        (CERTIFICATION, "Аттестация")
    )
    competition_id = models.AutoField(primary_key=True, db_column="id_мероприятия", verbose_name="id_мероприятия")
    certification_competition = models.CharField(max_length=20, choices=TYPE_COMPETITION,
                                                 db_column="Аттестация_соревнования",
                                                 verbose_name="Аттестация_соревнования")
    date = models.DateField(db_column="Дата", verbose_name="Дата")
    time = models.TimeField(db_column="Время", verbose_name="Время")
    place = models.CharField(max_length=50, db_column="Место_проведения", verbose_name="Место_проведения")
    coach_id = models.ForeignKey(to='Coach', on_delete=models.CASCADE, db_column="id_тренера(FK)",
                                 verbose_name="id_тренера(FK)")
    rating_id = models.ForeignKey(to='Rating', on_delete=models.CASCADE, db_column="id_рейтинга(FK)",
                                  verbose_name="id_рейтинга(FK)")
    cost = models.CharField(max_length=20, db_column="Стоимость", verbose_name="Стоимость")

    def __str__(self):
        return 'Мероприятие'

    class Meta:
        db_table = 'Мероприятия'
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Speaker(models.Model):
    """Выступающий """
    speaker_id = models.AutoField(primary_key=True, db_column="id_выступающего", verbose_name="id_выступающего")
    competition_id = models.ForeignKey(to='Competition', on_delete=models.CASCADE, db_column="id_мероприятия(FK)",
                                       verbose_name="id_мероприятия(FK)")
    entry = models.ForeignKey(to='Entry', on_delete=models.CASCADE, db_column="id_записи(FK)",
                              verbose_name="id_записи(FK)")

    def __str__(self):
        return "Выступающий"

    class Meta:
        db_table = 'Выступающий'
        verbose_name = 'Выступающий'
        verbose_name_plural = 'Выступающие'


class Coaching(models.Model):
    """Тренирующий"""
    coaching_id = models.AutoField(primary_key=True, db_column="id_тренерующегося", verbose_name="id_тренерующегося")
    practice_id = models.ForeignKey(to='Practice', on_delete=models.CASCADE, db_column="id_тренировки(FK)",
                                    verbose_name="id_тренировки(FK)")
    entry_id = models.ForeignKey(to='Entry', on_delete=models.CASCADE, db_column="id_записи(FK)",
                                 verbose_name="id_записи(FK)")

    def __str__(self):
        return 'Тренирующийся'

    class Meta:
        db_table = 'Тренирующийся'
        verbose_name = 'Тренирующий'
        verbose_name_plural = 'Тренирующие'


class Rating(models.Model):
    """Рейтинг"""
    rating_id = models.AutoField(primary_key=True, db_column="id_рейтинга", verbose_name="id_рейтинга")
    name = models.CharField(max_length=50, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Рейтинг'
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Coach(models.Model):
    """Тренер"""
    coach_id = models.AutoField(primary_key=True, db_column="id_тренера", verbose_name="id_тренера")
    surname = models.CharField(max_length=30, db_column="Фамилия", verbose_name="Фамилия")
    firstname = models.CharField(max_length=30, db_column="Имя", verbose_name="Имя")
    patronymic = models.CharField(max_length=30, db_column="Отчество", verbose_name="Отчество")
    phone_number = models.CharField(max_length=30, db_column="Телефон", verbose_name="Телефон")
    date_birth = models.DateField(db_column="Дата_рождения", verbose_name="Дата_рождения")
    date_enrollment = models.DateField(db_column="Дата_зачисления", verbose_name="Дата_зачисления")

    def __str__(self):
        return f'Тренер {self.surname}'

    class Meta:
        db_table = 'Тренер'
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


class Practice(models.Model):
    """Тренировки"""
    practice_id = models.AutoField(primary_key=True, db_column="id_тренеровки", verbose_name="id_тренеровки")
    coach = models.ForeignKey(to='Coach', on_delete=models.CASCADE, db_column="id_тренера(FK)",
                              verbose_name="id_тренера(FK)")
    date = models.DateField(db_column="Дата", verbose_name="Дата")
    time = models.TimeField(db_column="Время", verbose_name="Время")
    hall = models.ForeignKey(to='Hall', on_delete=models.CASCADE, db_column="id_зала(FK)", verbose_name="id_зала(FK)")
    cost = models.CharField(max_length=20, db_column="Стоимость", verbose_name="Стоимость")

    def __str__(self):
        return f"Тренировка тренера {self.coach.surname}"

    class Meta:
        db_table = 'Тренировки'
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'


class Hall(models.Model):
    """Зал"""
    hall_id = models.AutoField(primary_key=True, db_column="id_зала", verbose_name="id_зала")
    name = models.CharField(max_length=50, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Зал'
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'
