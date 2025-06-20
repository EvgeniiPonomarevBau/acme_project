# Generated by Django 5.2.2 on 2025-06-09 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0002_alter_birthday_birthday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='image',
            field=models.ImageField(blank=True, upload_to='birthdays_images', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='last_name',
            field=models.CharField(blank=True, help_text='Опциональное поле', max_length=20, verbose_name='Фамилия'),
        ),
    ]
