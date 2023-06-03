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

    year = models.SmallIntegerField(verbose_name='Год поступления', default=datetime.today().year)
    numgroup = models.SmallIntegerField(default=0, verbose_name='Номер группы', help_text='оставьте 0, если такая группа на потоке единственная')
    subgroup = models.SmallIntegerField(default=0, verbose_name='Подгруппа')
    is_foreigns = models.BooleanField(default=False, verbose_name='Иностранцы')

    def __str__(self):
        study_type = {
            'bachelors': ['БИЗ', 'БИО', 'ИВТ', 'ИС', 'М', 'МЕН', 'МТМ', 'МФ', 'ТД', 'ТФ', 'ХИМ', 'ХФМ', 'ЭКН', 'ЯФТ',
                          'ЯЭТ'],
            'specialists': ['АЭС', 'ЛД', 'ЭиА', 'ЯРМ'],
        }
        ans = self.type
        app_type = ''
        app_sub=''
        app_num=''
        if ans in study_type['bachelors']:
            app_type = f'-Б{self.year % 1000}'
        elif ans in study_type['specialists']:
            app_type = f'-С{self.year % 1000}'
        if self.numgroup:
            app_num = self.numgroup
        if self.subgroup:
            app_sub = f' (подгруппа {self.subgroup})'
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


