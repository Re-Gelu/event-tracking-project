# Generated by Django 4.0.8 on 2023-04-28 14:59

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_events_duration_events_visitors_list_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='registered_visitors',
        ),
        migrations.AddField(
            model_name='events',
            name='closing_registration_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время закрытия регистрации на мероприятие'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время проведения мероприятия'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='events',
            name='duration',
            field=models.DurationField(blank=True, default=datetime.timedelta(seconds=7200), max_length=datetime.timedelta(days=31), null=True, verbose_name='Длительность мероприятия'),
        ),
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.ImageField(blank=True, default='events_images/placeholder.jpg', null=True, upload_to='events_images/', verbose_name='Изображение для мероприятия'),
        ),
        migrations.AlterField(
            model_name='events',
            name='visitors_list',
            field=models.JSONField(auto_created=True, blank=True, default=list, editable=False, null=True, verbose_name='Зарегестрированные посетители мероприятия'),
        ),
    ]