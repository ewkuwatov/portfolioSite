# Generated by Django 4.2.3 on 2023-08-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('email', models.EmailField(max_length=300, verbose_name='Почта')),
                ('number', models.CharField(max_length=150, verbose_name='Номер')),
                ('comments', models.TextField(max_length=200, verbose_name='Комментарии')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('name', 'email', 'number', 'comments'),
            },
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ('package_name', 'package_price'), 'verbose_name': 'прайс', 'verbose_name_plural': 'Прайс'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('name', 'position'), 'verbose_name': 'человека', 'verbose_name_plural': 'Команда'},
        ),
    ]
