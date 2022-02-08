from tkinter import CASCADE
from django.db import models

class Scope (models.Model):
    name = models.CharField(max_length=60, verbose_name='Раздел')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Scope, through='Scopes', verbose_name="Тематика статьи", related_name="relation")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return f"{self.title}"

class Scopes (models.Model):
    tag = models.ForeignKey(Scope, on_delete= models.CASCADE, verbose_name="Раздел", related_name="scopes")
    article = models.ForeignKey(Article, on_delete= models.CASCADE, verbose_name="Статья", related_name="scopes")
    is_main = models.BooleanField(verbose_name="Основной тег",name="is_main")

    def __str__(self):
        return '{0}  {1}'.format(self.tag, self.is_main)
