# Generated by Django 4.1.3 on 2022-11-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['id'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новость'},
        ),
        migrations.AlterField(
            model_name='food',
            name='content',
            field=models.TextField(blank=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='food',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='food',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='food',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='food',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='food',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
    ]
