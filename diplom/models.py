from django.db import models


# Create your models here.
class Group(models.Model):
    data_formation = models.DateField(db_column='Дата формирования', verbose_name="Дата формирования")
    description = models.TextField(db_column="Описание", verbose_name="Описание")

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Entry(models.Model):
    group = models.ForeignKey(to='Group', on_delete=models.CASCADE, db_column="Группа", verbose_name="Группа")
    statement = models.ForeignKey(to='Statement', on_delete=models.CASCADE, db_column="Заявление", verbose_name="Заявление")

    def __str__(self):
        return f'Запись в группу {self.group.description}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Statement(models.Model):
    client = models.ForeignKey(to='Client', on_delete=models.CASCADE, db_column="Клиент", verbose_name="Клиент")
    type_statement = models.ForeignKey(to='TypeStatement', on_delete=models.CASCADE, db_column="Тип заявления", verbose_name="Тип заявления")
    data_statement = models.DateField(db_column="Дата заявления", verbose_name="Дата заявления")
    contract_number = models.CharField(max_length=20, db_column="Номер договора", verbose_name="Номер договора")
    data_start_contract = models.DateField(db_column="Дата начала договора", verbose_name="Дата начала договора")
    data_stop_contract = models.DateField(db_column="Дата окончания договора", verbose_name="Дата окончания договора")
    package_documents = models.ForeignKey(to='PackageDocuments', on_delete=models.CASCADE, db_column="Пакет документов", verbose_name="Пакет документов")
    payment_status = models.BooleanField(default=False, db_column="Статус оплаты", verbose_name="Статус оплаты")
    passport_series = models.CharField(max_length=20, db_column="Серия паспорта", verbose_name="Серия паспорта")
    passport_number = models.CharField(max_length=20, db_column="Номер паспорта", verbose_name="Номер паспорта")

    def __str__(self):
        return f'Заявление на {self.type_statement} от {self.client}'

    class Meta:
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'


class TypeStatement(models.Model):
    name = models.CharField(max_length=30, db_column="Тип заявления", verbose_name="Тип заявления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип заявления'
        verbose_name_plural = 'Типы заявления'


class PackageDocuments(models.Model):
    document = models.ManyToManyField(to='Document', db_column="Пакет документов", verbose_name="Пакет документов")

    def __str__(self):
        return 'Пакет документов'

    class Meta:
        verbose_name = 'Пакет документов'
        verbose_name_plural = 'Пакеты документов'


class Document(models.Model):
    name = models.CharField(max_length=50, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Client(models.Model):
    surname = models.CharField(max_length=30, db_column="Фамилия", verbose_name="Фамилия")
    firstname = models.CharField(max_length=30, db_column="Имя", verbose_name="Имя")
    patronymic = models.CharField(max_length=30, db_column="Отчество", verbose_name="Отчество")
    date_birth = models.DateField(db_column="Дата рождения", verbose_name="Дата рождения")
    phone_number = models.CharField(max_length=20, db_column="Номер телефона", verbose_name="Номер телефона")
    date_enrollment = models.DateField(db_column="Дата зачисления", verbose_name="Дата зачисления")
    growth = models.CharField(max_length=10, db_column="Рост", verbose_name="Рост")
    weight = models.CharField(max_length=10, db_column="Вес", verbose_name="Вес")

    def __str__(self):
        return f"Клиент {self.surname}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Achievements(models.Model):
    client = models.ForeignKey(to='Client', on_delete=models.CASCADE, db_column="Клиент", verbose_name="Клиент")
    rank = models.ForeignKey(to='Rank', on_delete=models.CASCADE, db_column="Разряд", verbose_name="Разряд")
    date_assignment = models.DateField(db_column="Дата присвоения", verbose_name="Дата присвоения")
    belt = models.ForeignKey(to='Belt', on_delete=models.CASCADE, db_column="Пояс", verbose_name="Пояс")
    competition = models.ForeignKey(to='Competition', on_delete=models.CASCADE, db_column="Соревнование", verbose_name="Соревнование")
    passport_number = models.CharField(max_length=20, db_column="Номер паспорта спортсмена", verbose_name="Номер паспорта спортсмена")

    def __str__(self):
        return f'Достижение клиента {self.client}'

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class Belt(models.Model):
    name = models.CharField(max_length=20, db_column="Пояс", verbose_name="Пояс")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пояс'
        verbose_name_plural = 'Пояса'
        ordering = ('name',)


class Rank(models.Model):
    name = models.CharField(max_length=50, db_column="Разряд", verbose_name="Разряд")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Разряд'
        verbose_name_plural = 'Разряды'


class Competition(models.Model):
    certification_competition = models.BooleanField(db_column="Аттестация", verbose_name="Аттестация")
    date = models.DateField(db_column="Дата", verbose_name="Дата")
    time = models.TimeField(db_column="Время", verbose_name="Время")
    place = models.CharField(max_length=50, db_column="Место проведения", verbose_name="Место проведения")
    coach_id = models.ForeignKey(to='Coach', on_delete=models.CASCADE, db_column="Тренер", verbose_name="Тренер")
    rating_id = models.ForeignKey(to='Rating', on_delete=models.CASCADE, db_column="Рейтинг", verbose_name="Рейтинг")
    cost = models.CharField(max_length=20, db_column="Стоимость", verbose_name="Стоимость")

    def __str__(self):
        return 'Мероприятие'

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятии'


class Speaker(models.Model):
    """Выступающий """
    competition_id = models.ForeignKey(to='Competition', on_delete=models.CASCADE, db_column="Мероприятие",
                                       verbose_name="Мероприятие")
    entry = models.ForeignKey(to='Entry', on_delete=models.CASCADE, db_column="Запись", verbose_name="Запись")

    def __str__(self):
        return "Выступающий"

    class Meta:
        verbose_name = 'Выступающий'
        verbose_name_plural = 'Выступающие'


class Coaching(models.Model):
    """Тренирующий"""
    practice_id = models.ForeignKey(to='Practice', on_delete=models.CASCADE, db_column="Тренировка",
                                    verbose_name="Тренировка")
    entry_id = models.ForeignKey(to='Entry', on_delete=models.CASCADE, db_column="Запись", verbose_name="Запись")

    def __str__(self):
        return 'Тренирующий'

    class Meta:
        verbose_name = 'Тренирующий'
        verbose_name_plural = 'Тренирующие'


class Rating(models.Model):
    """Рейтинг"""
    name = models.CharField(max_length=50, db_column="Рейтинг", verbose_name="Рейтинг")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Coach(models.Model):
    """Тренер"""
    surname = models.CharField(max_length=30, db_column="Фамилия", verbose_name="Фамилия")
    firstname = models.CharField(max_length=30, db_column="Имя", verbose_name="Имя")
    patronymic = models.CharField(max_length=30, db_column="Отчество", verbose_name="Отчество")
    phone_number = models.CharField(max_length=30, db_column="Номер телефона", verbose_name="Номер телефона")
    date_birth = models.DateField(db_column="Дата рождения", verbose_name="Дата рождения")
    date_enrollment = models.DateField(db_column="Дата зачисления", verbose_name="Дата зачисления")

    def __str__(self):
        return f'Тренер {self.surname}'

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


class Practice(models.Model):
    """Тренировки"""
    coach = models.ForeignKey(to='Coach', on_delete=models.CASCADE, db_column="Тренер", verbose_name="Тренер")
    date = models.DateField(db_column="Дата", verbose_name="Дата")
    time = models.TimeField(db_column="Время", verbose_name="Время")
    hall = models.ForeignKey(to='Hall', on_delete=models.CASCADE, db_column="Зал", verbose_name="Зал")
    cost = models.CharField(max_length=20, db_column="Стоимость", verbose_name="Стоимость")

    def __str__(self):
        return f"Тренировка тренера {self.coach.surname}"

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'


class Hall(models.Model):
    """Зал"""
    name = models.CharField(max_length=50, db_column="Название зала", verbose_name="Название зала")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'
