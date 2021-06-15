from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField('contents')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "Новости"
        verbose_name = "Новость"

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    sender = models.EmailField()
    message = models.TextField()
    copy = models.BooleanField()
    
    class Meta:
        verbose_name_plural = "Обращения"
        verbose_name = "Обращение"
    

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Комментарий от {} к новости {}'.format(self.author_id, self.post)
        
    class Meta:
        verbose_name_plural = "Комментарии"
        verbose_name = "Комментарий"
        
class Specialization (models.Model):
    specialization = models.CharField(verbose_name='Специализация', max_length=300)

    def __str__(self):
        return '%s ' % self.specialization

    class Meta:
        verbose_name_plural = "Специализации"
        verbose_name = "Специализация"

class Doctor (models.Model):
    name=models.CharField(verbose_name='ФИО', max_length = 300 ) 
    specialization=models.ForeignKey(Specialization, verbose_name='Специализация', on_delete=models.CASCADE)
    info=models.CharField(verbose_name='Информация о враче',max_length=10000)

    def __str__(self):
        return '%s ' % self.name

    class Meta:
        verbose_name_plural = "Врачи"
        verbose_name = "Врач"


class Reception(models.Model):
    specialization = models.ForeignKey(Specialization, verbose_name='Специализация', on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor, verbose_name='Врач', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата приема ')
    time=models.CharField(verbose_name='Время приема ', max_length=5)
    patient_name=models.CharField(verbose_name='ФИО ', max_length=300)
    patient_info=models.CharField(verbose_name='Информация о пациенте ', max_length=10000)

    def __str__(self):
        return 'Прием № %s' % self.id

    class Meta:
        verbose_name_plural = "Приемы"
        verbose_name = "Прием"