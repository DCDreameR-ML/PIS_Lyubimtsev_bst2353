from django.conf import settings
from django.db import models

class Article(models.Model):
    title = models.CharField('Заголовок', max_length=200, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name='Автор')
    text = models.TextField('Текст')
    created_date = models.DateField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.author.username}: {self.title}'

    def get_excerpt(self):
        return self.text[:140] + ('...' if len(self.text) > 140 else '')
