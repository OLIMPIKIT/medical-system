from django.db import models
from django.conf import settings

class Profile(models.Model):
    GENDER_CHOICES=(('M', u'Мужcкой'),('F', u'Женский'))
    ROLE_CHOICES=(('0', u'Пациент'),('1', u'Врач'),('2', u'Регистратор'), ('3', u'Администратор'))
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    role = models.CharField(max_length=40, blank=True, verbose_name=(u'Роль'), choices=ROLE_CHOICES)
    surname = models.CharField(max_length=50, blank=True, verbose_name=(u'Фамилия'))
    firstname = models.CharField(max_length=50, blank=True, verbose_name=(u'Имя'))
    patronym = models.CharField(max_length=50, blank=True, verbose_name=(u'Отчество'))
    gender = models.CharField(max_length=40, blank=True, verbose_name=(u'Пол'), choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=(u'Дата рождения (пример: дд.мм.гггг)'))
    snils = models.CharField(max_length=11, blank=True, verbose_name=(u'Номер СНИЛС'))
    passport = models.CharField(max_length=10, blank=True, verbose_name=(u'Серия и номер паспорта'))
    adress = models.CharField(max_length=300, blank=True, verbose_name=(u'Адрес'))
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name=(u'Телефон'))

    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)
        
    class Meta:
        verbose_name_plural = "Профили"
        verbose_name = "Профиль"