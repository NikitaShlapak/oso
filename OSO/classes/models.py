from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class StudyGroup(models.Model):
    class StudyGroupType(models.TextChoices):
        AES = 'АЭС', 'АЭС'
        EIA = 'ЭиА', 'ЭиА'
        YARM = 'ЯРМ', 'ЯРМ'
        BIZ = 'БИЗ', 'БИЗ'
        BIO = 'БИО', 'БИО'
        IVT = 'ИВТ', 'ИВТ'
        IS = 'ИС', 'ИС'
        M = 'М', 'М'
        MEN = 'МЕН', 'МЕН'
        MTM = 'МТМ', 'МТМ'
        MF = 'МФ', 'МФ'
        TD = 'ТД', 'ТД'
        TF = 'ТФ', 'ТФ'
        HIM = 'ХИМ', 'ХИМ'
        HFM = 'ХФМ', 'ХФМ'
        EKN = 'ЭКН', 'ЭКН'
        YAFT = 'ЯФТ', 'ЯФТ'
        YAET = 'ЯЭТ', 'ЯЭТ'
        TEACHER = 'Преподаватель', 'Преподаватель'
        OUTSIDER = 'Внешний менеджер', 'Внешний менеджер'

    type = models.CharField(max_length=50, verbose_name='Тип группы',choices=StudyGroupType.choices, default=StudyGroupType.OUTSIDER)

    class StudyGroupCourseType(models.TextChoices):
        SPEC = 'С', 'Специалитет'
        BACH = 'Б', 'Бакалавриат'
        MAG = 'М', 'Магистратура'
        ASP = 'А', 'Аспирантура'

        OTHER = '', 'Другое'

    course = models.CharField(max_length=50, verbose_name='Программа обучения',choices=StudyGroupCourseType.choices, default=StudyGroupCourseType.OTHER)

    class StudyGroupInstituteType(models.TextChoices):
        YaFIT = 'оЯФиТ', 'отделение ядерной физики и технологий'
        OBT = 'ОБТ', 'отделение биотехнологий'
        SEN = 'СЭН', 'социально-экономическое направление'
        IKS = 'ИИКС', 'институт интеллектуальных и кибернетических систем'

        OTHER = '', 'Другое'

    course = models.CharField(max_length=50, verbose_name='Программа обучения', choices=StudyGroupInstituteType.choices,
                              default=StudyGroupInstituteType.OTHER)

    year = models.SmallIntegerField(verbose_name='Год поступления', default=datetime.today().year)
    numgroup = models.SmallIntegerField(default=0, verbose_name='Номер группы', help_text='оставьте 0, если такая группа на потоке единственная')
    timetable_id = models.IntegerField(default=111, verbose_name='id группы в расписании')
    is_foreigns = models.BooleanField(default=False, verbose_name='Иностранцы')


    def __str__(self):

        ans = self.type

        app_sub=''
        app_num=''
        app_type = f'-{self.course}{self.year % 1000}'

        if self.numgroup:
            app_num = self.numgroup

        ans = ans + f"{app_num}{app_type}{app_sub}"
        if self.is_foreigns:
            ans = ans+'и'
        return ans

    def get_study_year(self):
        dif = datetime.today().year - self.year
        if 1< datetime.today().month<8:
            dif = dif+1
        return dif

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'


