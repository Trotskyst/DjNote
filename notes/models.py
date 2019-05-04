from django.db import models


class Note(models.Model):
    label = models.CharField(max_length=200, verbose_name="Заголовок заметки")
    body = models.TextField(verbose_name="Текст заметки")
    timestamp = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='notes', blank = True, verbose_name="Теги", error_messages={'invalid':'Enter a valid phone number'})

    # def __unicode__(self):
    #     return self.label


class Tag(models.Model):
    label = models.CharField(max_length=200, verbose_name="Тег", unique=True)

    class Meta:
        ordering = ['label',]

    def __str__(self):
        return self.label

    def __unicode__(self):
        return self.label
