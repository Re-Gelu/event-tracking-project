# Generated by Django 4.0.8 on 2023-05-16 10:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0020_alter_events_options_alter_eventtypes_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='visitors',
            field=models.ManyToManyField(blank=True, limit_choices_to={'eventregistrations__is_invitation_accepted': True}, through='events.EventRegistrations', to=settings.AUTH_USER_MODEL, verbose_name='Зарегестрированные на мероприятие пользователи'),
        ),
    ]
