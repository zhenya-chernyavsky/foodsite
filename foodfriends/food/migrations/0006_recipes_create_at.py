# Generated by Django 4.1.3 on 2022-11-25 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_recipes_alter_food_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
    ]
