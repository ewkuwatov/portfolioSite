from django.db import models

# Create your models here.

class Testimonial(models.Model):
    description = models.TextField('Описание', max_length=1000, blank=True)
    name = models.CharField('Имя', max_length=150, db_index=True)
    position = models.CharField('Должность', max_length=150, db_index=True)

    class Meta:
        ordering = ('name', 'position')
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField('Имя', max_length=150, db_index=True)
    position = models.CharField('Должность', max_length=150, db_index=True)
    image = models.ImageField(upload_to='static/images/team', blank=True)
    urls_facebook = models.CharField('Профиль Facebook', max_length=150, db_index=True)
    urls_telegram = models.CharField('Профиль Телеграм', max_length=150, db_index=True)
    urls_linkedin = models.CharField('Профиль Линкедин', max_length=150, db_index=True)
    urls_instagram = models.CharField('Профиль Инстаграма', max_length=150, db_index=True)


    class Meta:
        ordering = ('name', 'position')
        verbose_name = 'человека'
        verbose_name_plural = 'Команда'

        def __str__(self):
            return self.name

class Price(models.Model):
    package_name = models.CharField('Название пакета', max_length=150)
    package_price = models.CharField('Цена', max_length=150)


    class Meta:
        ordering = ('package_name', 'package_price')
        verbose_name = 'прайс'
        verbose_name_plural = 'Прайс'

        def __str__(self):
            return self.name

class Contact(models.Model):
    name = models.CharField('Имя', max_length=150)
    email = models.EmailField('Почта', max_length=300)
    number = models.CharField('Номер', max_length=150)
    comments = models.TextField('Комментарии', max_length=200)

    class Meta:
        ordering = ('name', 'email', 'number', 'comments')
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'

