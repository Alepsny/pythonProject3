# Generated by Django 4.0.4 on 2022-05-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['-created_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
