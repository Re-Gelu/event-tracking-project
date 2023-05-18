# Generated by Django 4.2.1 on 2023-05-15 22:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0018_remove_eventregistrations_event_user_id_unique_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="events",
            old_name="category_id",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="events",
            old_name="venue_id",
            new_name="venue",
        ),
        migrations.RenameField(
            model_name="paidevents",
            old_name="category_id",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="paidevents",
            old_name="venue_id",
            new_name="venue",
        ),
        migrations.RenameField(
            model_name="privateevents",
            old_name="category_id",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="privateevents",
            old_name="venue_id",
            new_name="venue",
        ),
    ]