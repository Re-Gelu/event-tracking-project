# Generated by Django 4.0.8 on 2023-04-29 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0005_remove_events_registered_visitors_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='date',
            new_name='start_datetime',
        ),
        migrations.RemoveField(
            model_name='events',
            name='visitors_list',
        ),
        migrations.CreateModel(
            name='EventsRegistrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации на мероприятие')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления регистрации на мероприятие')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]