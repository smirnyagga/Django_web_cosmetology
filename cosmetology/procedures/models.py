from django.db import models
from django.urls import reverse


class Categories(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото категории')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL', db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('procedures_of_category', kwargs={'cat_slug': self.slug})


class Procedures(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='URL', db_index=True, unique=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(null=True, blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    results = models.TextField(null=True, blank=True, verbose_name='Результаты')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    time = models.CharField(null=True, blank=True, max_length=100, verbose_name='Продолжительность')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    categories = models.ManyToManyField(Categories, related_name='procedures', through='Relation')

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедры'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('procedure_detail', kwargs={'proc_slug': self.slug})


class Relation(models.Model):
    procedure = models.ForeignKey(Procedures, related_name='relation', on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, related_name='relation', on_delete=models.CASCADE)


class Doctors(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото')

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    def __str__(self):
        return self.name


class Applications(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    email = models.EmailField(verbose_name='E-mail')
    message = models.TextField(verbose_name='Ваш вопрос')

    class Meta:
        verbose_name = 'Заявка на процедуру'
        verbose_name_plural = 'Заявки на процедуры'

    def __str__(self):
        return self.name


class Questions(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    question = models.TextField(verbose_name='Вопрос')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    answer = models.TextField(null=True, blank=True, verbose_name='Ответ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        verbose_name = 'Вопросы и отзывы'
        verbose_name_plural = 'Вопросы и отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
